#!/usr/bin/python
import os,sys,time,getopt,tempfile,signal,shlex
from stat import *

DEBUG=False

# TODO
# Add a function to check for working ssh without password to the 
# destination.

# ERROR Return Codes
# Backup Sucessfull
BACKOK=0
# Backup is locked
BACKLOCKED=1
# Backup support programs not installed
BACKNOSUPPORT=2
# Backup method not supported
BACKMETHODUS=4
# Suspend failed
BACKSUSPENDFAIL=8
# VMware Snapshot filed
BACKVMSNAPFILE=16
# Not enough LVM VG space
BACKNOVGSPACE=32
# LVM Snapshot Failed
BACKLVMSNAPFAIL=64
# VM Not on LVM Volume
BACKNOTONLVM=128
# Restore Sucessfull
RESTOK=0
#Invalid Archive
RESTINVALID=1
#Unsupported Archive
RESTUNSUPPORTED=2

if os.path.isdir('/var/lock'):
    LOCKFILE='/var/lock/vmbackup.lock'
else:
    LOCKFILE='/Applications/vmbackup.app/Contents/Resources/var/lock/vmbackup.lock'
if os.path.isdir('/var/log/vmbackup'):
    LOGFILE='/var/log/vmbackup/vmbackup.log'
else:
    if os.path.isdir('/Applications/vmbackup.app/Contents/Resources/var/log/vmbackup.log'):
        LOGFILE='/Applications/vmbackup.app/Contents/Resources/var/log/vmbackup.log'
    else:
        LOGFILE='/tmp/vmbackup.log'

# LVM defaults
VMVG='datastore'
VMLV='datastore'
VGMINFREEPE=int(256)
VGSNAPSHOTSIZE='4G'

class PROGRAMS:
    def __init__(self):
        self.commands={'vmware': '/usr/bin/vmware','vmware-cmd': '/usr/bin/vmware-cmd','vmrun': '','su':'/usr/bin/su','ps':'/usr/bin/ps','df':'/usr/bin/df','vgdisplay':'/sbin/vgdisplay','lvcreate':'/sbin/lvcreate','mount':'/bin/mount','umount':'/bin/umount','lvremove':'/sbin/lvremove','tar':'/bin/tar','ssh':'/usr/bin/ssh','vmkfstools':'','mkisofs':'/usr/bin/mkisofs','id':'/usr/bin/id','zip':'/usr/bin/zip','unzip':'/usr/bin/unzip','cp':'/bin/cp','gzip':'/bin/gzip','bzip2':'/bin/bzip2','smbmount':'/usr/bin/smbmount','du':'/usr/bin/du','VBoxManage':'/usr/bin/VBoxManage','vboxmanage':'/usr/bin/vboxmanage'}
        self.path=['/usr/bin','/bin','/usr/sbin','/sbin']
        self.updatepaths()
    def updatepaths(self):
        rc=0
        for program in self.commands.keys():
            self.commands[program]=''
            for dir in self.path:
                temp=os.path.join(dir,program)
                if os.path.exists(temp):
                    self.commands[program]=temp
                    break
            if self.commands[program] == '':
                rc=1
        return(rc)
    def iscommand(self,command):
        if self.commands[command] == '':
            return False
        else:
            return True
    def system(self,program,options):
        try:
            # Unlike the normal system call I am returning the normal program return code
            #print 'Running: %s %s' % (self.commands[program],options)
            return os.system('%s %s' % (self.commands[program],options)) >> 8
        except KeyError:
            return -1
    def popen(self,program,options):
        #print 'Running: %s %s' % (self.commands[program],options)
        if self.iscommand(program):
            return os.popen('%s %s' % (self.commands[program],options))
        else:
            return False

def getproductinfo():
    product='none'
    version=0
    programs=PROGRAMS()
    if programs.iscommand('vmware'):
        temp=programs.popen('vmware','-v 2>/dev/null').readlines()[0]
        splittemp=temp.strip().split()
        if ' '.join(splittemp[:2]) == 'VMware Server':
            product='vmware_server'
        if ' '.join(splittemp[:2]) == 'VMware Workstation':
            product='vmware_workstation'
    if product == 'none' and os.path.exists('/Applications/VMware Fusion.app/Contents/MacOS/vmware'):
        product='vmware_fusion'
        return product,1
    if product == 'none' and (programs.iscommand('VBoxManage') or programs.iscommand('vboxmanage')):
        product='virtualbox'
        return product,1
    version=int(splittemp[2].split('.')[0])
    return product,version

def getproductsinfo():
    product=[]
    version=0
    programs=PROGRAMS()
    if programs.iscommand('vmware'):
        temp=programs.popen('vmware','-v 2>/dev/null').readlines()[0]
        splittemp=temp.strip().split()
        if ' '.join(splittemp[:2]) == 'VMware Server':
            version=int(splittemp[2].split('.')[0])
            product.append(['vmware_server',version])
        if ' '.join(splittemp[:2]) == 'VMware Workstation':
            version=int(splittemp[2].split('.')[0])
            product.append(['vmware_workstation',version])
    if os.path.exists('/Applications/VMware Fusion.app/Contents/MacOS/vmware'):
        product.append(['vmware_fusion',1])
    if programs.iscommand('VBoxManage') or programs.iscommand('vboxmanage'):
        product.append(['virtualbox',1])
    return product

def isproductinstalled(product='none',version=0):
    for prod,ver in getproductsinfo():
        if product == prod and (version == 0 or ver == version):
            return True
    return False

def recursivedirlist(dirname):
    listing=[]
    if os.path.isdir(dirname):
        for f in os.listdir(dirname):
            pathname = os.path.join(dirname, f)
            try:
                mode = os.stat(pathname)[ST_MODE]
                if S_ISDIR(mode):
                    listing=listing+recursivedirlist(pathname)
                else:
                    listing.append(pathname)
            except OSError:
                pass
    return listing

def getvmlist():
        listing=[]
        programs=PROGRAMS()
        VMPATH=['/var/lib/vmware/Virtual Machines','~/vmware']
        if programs.commands['vmware-cmd'] !='':
            for vms in programs.popen('vmware-cmd','-l').readlines():
                listing.append(vms.strip())
        if len(listing) == 0 and os.path.exists('/etc/vmware/vm-list'):
            for line in open('/etc/vmware/vm-list','r').readlines():
                splitline=shlex.split(line.strip())
                if splitline.lower() == 'config':
                    listing.append(string.join(splitline[1:]))
        if len(listing) == 0:
            if programs.commands['vmrun'] != '':
                for vms in programs.popen('vmrun','2> /dev/null list').readlines():
                    if vms.find('.vmx') != -1:
                        #listing.append('/'.join(vms.strip().split('/')[-2:]))
                        listing.append(vms.strip())
        if programs.commands['VBoxManage'] != '':
            for temp in programs.popen('VBoxManage','list vms|grep Name').readlines():
                listing.append('Virtualbox:%s' % temp.strip().split(':')[1].strip())
        if programs.commands['vboxmanage'] != '':
            for temp in programs.popen('vboxmanage','list vms|grep Name').readlines():
                listing.append('Virtualbox:%s' % temp.strip().split(':')[1].strip())
        # TODO: vmrun and vmware fusion only know about running VMs.  So we need to also search
        # the VMPath for .vmx files of non-running VMs when vmrun is used
        product,version=getproductinfo()
        if product == 'vmware_fusion' or product == 'vmware_workstation':
            for directory in VMPATH:
                for file in recursivedirlist(os.path.expanduser(directory)):
                    if file[-4:] == '.vmx':
                        listing.append(file)
        return listing

def getvmname(configfile,addconfigfile=False):
    programs=PROGRAMS()
    if configfile[:11] == 'Virtualbox:' and len(configfile) > 11:
        return(configfile[11:])
    if programs.iscommand('vmware-cmd'):
        name=''
        try:
            name=programs.popen('vmware-cmd','"%s" getconfig displayName' % configfile).readlines()[0].strip().split('=')[1].strip()
            if addconfigfile==True:
                name=name+ ' ('+configfile+')'
        except IndexError:
            pass
        if name != '':
            return name
    vmname=os.path.basename(configfile)
    if os.path.exists(configfile):
        for line in open(configfile,'r').readlines():
            splitline=line.strip().split('=')
            if len(splitline) == 2:
                if splitline[0].strip().lower() == 'displayname':
                    vmname=splitline[1].replace('"','').strip().lower()
    return vmname

class vm:
    def __init__(self,configfile='', vmname='', destdir='.'):
        self.configfile=configfile
        self.destdir=destdir
        self.childpid=0
        self.user='root'
        self.snapshotname='vmbackup_snapshot'
        self.backuplist=[]
        self.programs=PROGRAMS()
        # Determine the product the VM we are working with runs under
        if len(configfile) > 11 and configfile[:11] == 'Virtualbox:':
            vmname=configfile[11:]
            self.product='virtualbox'
            self.version=1
            self.snapshotname='vmbackup_snapshot_%d' % os.getpid()
            if self.programs.iscommand('VBoxManage'):
                for line in self.programs.popen('VBoxManage','showvminfo "%s"' % vmname):
                    splitline=line.strip().split(':')
                    if splitline[0] in ('Config file','Primary master','Secondary Master'):
                        temp=splitline[1].split('(')[0].strip()
                        self.backuplist.append(temp)
        else:
            self.product,self.version=getproductinfo()
        if vmname == '' and configfile != '':
            self.vmname=os.path.basename(configfile)
            for line in open(configfile,'r').readlines():
                splitline=line.strip().split('=')
                if len(splitline) == 2:
                    if splitline[0].strip().lower() == 'displayname':
                        self.vmname=splitline[1].replace('"','').strip().lower()
                        break
        else:
            self.vmname=vmname
    def dump(self):
        print 'Configfile: %s\tVMname: %s\tState: %s' % (self.configfile,self.vmname,self.getstate())
    def getstate(self):
        if self.product == 'virtualbox':
            if self.programs.iscommand('VBoxManage') and self.configfile[:11] == 'Virtualbox:':
                splitcmd=self.programs.popen('VBoxManage','showvminfo "%s"|grep State' % (self.configfile[11:])).readlines()[0].strip().split(':')
                if len(splitcmd):
                    state=splitcmd[1].split()[0]
                    if state == 'running':
                        return 'on'
                    if state == 'paused':
                        return 'suspended'
                    if state == 'aborted':
                        return 'off'
            return 'off'
        else:
            if self.programs.commands['vmware-cmd']!='':
                splitcmd=self.programs.popen('vmware-cmd','"%s" getstate' % (self.configfile)).readlines()[0].strip().split('=')
                if len(splitcmd):
                    return splitcmd[1].strip()
                else:
                    print 'Error bad output from vmware-cmd',splitcmd
                    return 'unknown'
                #return(self.programs.popen('vmware-cmd','"%s" getstate' % (self.configfile)).readlines()[0].strip().split('=')[1].strip())
            if self.programs.commands['vmrun']!='':
                for line in self.programs.popen('vmrun','2>/dev/null list').readlines():
                    if line.strip() == self.configfile:
                        return('on')
                for line in open(self.configfile,'r').readlines():
                    splitline=line.split('=')
                    if splitline[0].strip().lower() == 'checkpoint.vmstate' and splitline[1].strip() != '""':
                        return('suspended')
            return('off')
    def suspend(self):
        # Before we suspend we need to store the user the VM is running as
        # so we can run the resume as the correct user.
        if self.product == 'vmware_workstation':
            user=self.programs.popen('ps','-C vmware-vmx -o user').readlines()[-1]
            if user != 'USER':
                self.user=user
        if self.product == 'vmware_fusion':
            if os.path.exists('/Applications/vmware_suspend.app/Contents/MacOS/applet'):
                ret=os.system('/Applications/vmware_suspend.app/Contents/MacOS/applet')
                return(0)
            if os.path.exists('vmware_suspend.app/Contents/MacOS/applet'):
                ret=os.system('vmware_suspend.app/Contents/MacOS/applet')
                return(0)
            return(1)
        if self.product == 'virtualbox':
            if self.programs.iscommand('VBoxManage'):
                self.programs.system('VBoxManage','controlvm "%s" pause' % self.configfile[11:])
            else:
                if self.programs.iscommand('vboxmanage'):
                    self.programs.system('vmboxmanage','controlvm "%s" pause' % self.configfile[11:])
        if self.product in ("vmware_server","vmware_workstation","vmware_esx"):
            if self.programs.iscommand('vmware-cmd'):
                ret=self.programs.popen('vmware-cmd','> /dev/null 2>&1 "%s" suspend' % self.configfile).readlines()
            if self.programs.iscommand('vmrun'):
                self.programs.system('vmrun','>/dev/null 2>&1 suspend "%s"' % self.configfile)
        if self.getstate() == 'suspended' or self.getstate() == 'off':
            return(0)
        else:
            return(1)
    def resume(self):
        if self.product == 'vmware_fusion':
            if os.path.exists('/Applications/vmware_resume.app/Contents/MacOS/applet'):
                ret=os.system('/Applications/vmware_resume.app/Contents/MacOS/applet')
                return(0)
            if os.path.exists('vmware_resume.app/Contents/MacOS/applet'):
                ret=os.system('vmware_resume.app/Contents/MacOS/applet')
                return(0)
            return(1)
        if self.product == 'virtualbox':
            if self.programs.iscommand('VBoxManage'):
                self.programs.system('VBoxManage','controlvm "%s" resume' % self.configfile[11:])
            else:
                if self.programs.iscommand('vboxmanage'):
                    self.programs.system('vmboxmanage','controlvm "%s" resume' % self.configfile[11:])
        if self.product in ("vmware_server","vmware_workstation","vmware_esx"):
            if self.programs.iscommand('vmware-cmd'):
                ret=self.programs.popen('vmware-cmd','"%s" start' % self.configfile).readlines()
            else:
                if self.programs.iscommand('vmrun'):
                    if self.user != 'root':
                        ret=self.programs.system('su','-c "vmrun >/dev/null 2>&1 start \"%s\"" %s' % (self.configfile,self.user))
                    else:
                        ret=self.programs.system('vmrun','>/dev/null 2>&1 start "%s"' % self.configfile)
                    return('on')
        return(self.getstate())
    def takesnapshot(self):
        if self.product == 'virtualbox':
            if self.programs.iscommand('VBoxManage'):
                self.programs.system('VBoxManage','snapshot "%s" take %s' % (self.configfile[11:],self.snapshotname))
            if self.programs.iscommand('vboxmanage'):
                self.programs.system('vboxmanage','snapshot "%s" take %s' % (self.configfile[11:],self.snapshotname))
            return(0)
        if self.programs.iscommand('vmrun'):
            ret=self.programs.popen('vmrun','2>/dev/null snapshot "%s" vmbackup' % self.configfile).readlines()
            return(0)
        else:
            return(1)
    def delsnapshot(self):
        if self.product == 'virtualbox':
            if self.programs.iscommand('VBoxManage'):
                self.programs.system('VBoxManage','snapshot "%s" discard %s' % (self.configfile[11:],self.snapshotname))
            if self.programs.iscommand('vboxmanage'):
                self.programs.system('vboxmanage','snapshot "%s" discard %s' % (self.configfile[11:],self.snapshotname))
            return(0)
        if self.programs.iscommand('vmrun'):
            self.programs.system('vmrun','2>/dev/null deletesnapshot "%s" vmbackup' % self.configfile)
            return(0)
        else:
            return(1)
    def revertsnapshot(self):
        # I don't understand how this can be done for Virtualbox
        if self.programs.iscommand('vmrun'):
            self.programs.system('vmrun','2>/dev/null revertToSnapshot "%s"' % self.configfile)
            return(0)
        return(1)
    def waitforlock(self,timeoutsecs=0):
        endtime=time.time()+float(timeoutsecs)
        while (self.islocked()):
            if timeoutsecs != 0:
                if time.time() > endtime:
                    return self.islocked()
            time.sleep(5)
        return self.lock()
    def lock(self):
        fh=open(LOCKFILE,'w')
        fh.write('%d\n' % os.getpid())
        return self.islocked()
    def islocked(self):
        if os.path.exists(LOCKFILE):
            try:
                lockpid=int(open(LOCKFILE,'r').readlines()[0].strip())
                if lockpid == os.getpid():
                    return True
                else:
                    pids=[]
                    for line in os.popen('/bin/ps ax').readlines()[1:]:
                        splitline=line.strip().split()
                        if len(splitline):
                           pids.append(int(splitline[0]))
                    if lockpid not in pids:
                        self.unlock()
                        return False
            except IndexError:
                return True
        return False
    def unlock(self):
        os.remove(LOCKFILE)

    def NoOutput(self,percent,text):
        print '%d percent complete - %s' % (percent,text)

    def backup(self,archiveformat='tgz',lvmconfigpath='',destdir='',mountpoint='',checklock=False, callback=0, backupmethod='Cold'):
        if callback == 0:
            callback=self.NoOutput
        callback(10,'Backup of %s starting' % self.vmname)
        if not os.path.exists(os.path.dirname(LOGFILE)):
            os.mkdir(os.path.dirname(LOGFILE))
        if checklock and self.islocked():
            return(BACKLOCKED)
        if checklock:
            self.lock()
        desthost=''
        cwd=os.getcwd()
        if destdir == '':
            destdir=self.destdir
        if destdir == '.':
            destdir=cwd
        temp=destdir.split(':')
        if (len(temp)>1):
            destdir=temp[1]
            desthost=temp[0]
        if lvmconfigpath == '':
            sourcedir=os.path.dirname(self.configfile)
        else:
            sourcedir=os.path.dirname(lvmconfigpath)
        archiveheaderfile='vmbackup_info.%d' % os.getpid()
        file=open(archiveheaderfile,'w')
        file.write('ArchiveFormat: 1\n')
        file.write('BackupMethod: %s\n' % backupmethod)
        file.write('VMType: %s\n' % self.product)
        file.write('VMName: %s\n' % self.vmname)
        file.close()
        self.backuplist.append(archiveheaderfile)
        filelistfile='/tmp/vmbackup_filelist.%d' % os.getpid()
        file=open(filelistfile,'w')
        for filename in self.backuplist:
            file.write('%s\n' % filename)
        file.close()
        command=['tar','>> %s 2>&1 -cf "%s/%s.%s.tar" -T "%s" "%s"'  % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),filelistfile,sourcedir)]
        if desthost == '':
            if archiveformat == 'tar':
                command=['tar','>> %s 2>&1 -cf "%s/%s.%s.tar" -T "%s" "%s"'  % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),filelistfile,sourcedir)]
            if archiveformat == 'tgz':
                command=['tar','>> %s 2>&1 -czf "%s/%s.%s.tar.gz" -T "%s" "%s"'  % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),filelistfile,sourcedir)]
            if archiveformat == 'bz2':
                command=['tar','>> %s 2>&1 -cjf "%s/%s.%s.tar.bz2" -T "%s" "%s"'  % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),filelistfile,sourcedir)]
            # The Zip, dir and iso formats needs support for the filelist functionality added
            if archiveformat == 'zip':
                command=['zip','>> %s 2>&1 -r "%s/%s.%s.zip" "%s"' % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),sourcedir)]
            if archiveformat == 'dir':
                command=['cp',' -a "%s" "%s"' % (sourcedir,destdir)]
            if archiveformat == 'iso':
                command=['mkisofs','>> %s 2>&1 -o "%s/%s.%s.iso" -R -J "%s"' % (LOGFILE,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'),sourcedir)]
        else:
            if archiveformat == 'tar':
                command=['tar','-cf - -T "%s" "%s"|%s %s "cat > \"%s/%s.%s.tar\""' % (filelistfile,sourcedir,self.programs.commands['ssh'],desthost,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))]
            if archiveformat == 'tgz':
                command=['tar','-czf - -T "%s" "%s"|%s %s "cat > \"%s/%s.%s.tar.bz2\""' % (filelistfile,sourcedir,self.programs.commands['ssh'],desthost,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))]
            if archiveformat in ('bz2','tbz2','tar.bz2','bzip'):
                command=['tar','-cjf - -T "%s" "%s"|%s %s "cat > \"%s/%s.%s.tar.bz2\""' % (filelistfile,sourcedir,self.programs.commands['ssh'],desthost,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))]
            # The Zip and dir formats need support for the filelist functionality added
            if archiveformat == 'zip':
                command=['zip','-r - "%s"|%s %s "cat > \"%s/%s.%s.zip\""' % (sourcedir,self.programs.commands['ssh'],desthost,destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))]
            if archiveformat == 'dir':
                splitpath=sourcedir.split('/')
                pathlen=len(splitpath)
                command=['tar','-cf - "%s"|%s %s "(cd \"%s\";tar -C \"%s\" --strip %d -xf - )"' % (sourcedir,self.programs.commands['ssh'],desthost,destdir,destdir,pathlen-2)]
        pid=os.fork()
        if pid == 0:
            if mountpoint != '':
                os.chdir(mountpoint)
            self.programs.system(command[0],command[1])
            os.chdir(cwd)
            if checklock:
                self.unlock()
            os._exit(BACKOK)
        else:
            childpid=0
            if self.product == 'virtualbox':
                dusize=0
                for file in self.backuplist:
                    dusize=dusize+(os.path.getsize(file)/1024)
            else:
                dusize=long(os.popen('du -sk "%s"' % os.path.dirname(self.configfile)).readlines()[0].strip().split()[0])
            currentsize=0
            # The estimated size will be about the dusize for non-compressed formats (tar and iso)
            estsize=dusize
            if archiveformat == 'tar':
                outfile='%s/%s.%s.tar' % (destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))
            if archiveformat == 'iso':
                outfile='%s/%s.%s.iso' % (destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))
            if archiveformat == 'tgz':
                estsize=dusize/2.8
                outfile='%s/%s.%s.tar.gz' % (destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))
            if archiveformat in ('bz2','tbz2','tar.bz2','bzip'):
                estsize=dusize/3.1
                outfile='%s/%s.%s.tar.bz2' % (destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))
            if archiveformat == 'zip':
                estsize=dusize/3.1
                outfile='%s/%s.%s.zip' % (destdir,self.vmname,time.strftime('%Y%m%d%H%M%S'))
            vmdir=destdir
            if self.product != 'virtualbox':
                try:
                    vmdir='%s/%s' % (destdir,os.path.basename(sourcedir).split()[-1])
                except KeyError:
                    pass
            while (childpid == 0):
                try:
                    childpid,status=os.waitpid(pid,os.WNOHANG)
                except OSError:
                    childpid=0
                time.sleep(10)
                if desthost == '':
                    if archiveformat == 'dir':
                        if DEBUG:
                            callback(50,'DEBUG: Running: du -sk "%s"' % (vmdir))
                            print
                            sys.stdout.flush()
                        duout=self.programs.popen('du','-sk "%s"' % (vmdir)).readlines()
                        if len(duout):
                            temp=duout[0].strip().split()[0]
                            if DEBUG:
                                print temp
                                sys.stdout.flush()
                            currentsize=long(temp)
                        else:
                            currentsize=long(dusize)/2
                    else:
                        if os.path.isfile(outfile):
                            currentsize=os.path.getsize(outfile)/1024
                    percentage=10+int((float(currentsize)/float(dusize)) * 80)
                    callback(percentage,'Running backup %s -> %s' % (sourcedir,destdir))
                else:
                    callback(50,'Backup of %s to Remote host running' % self.vmname)
            os.unlink(archiveheaderfile)
            os.unlink(filelistfile)
            return(status)
    def backup_suspend(self,archiveformat='tgz',destdir='',checklock=False, callback=0):
        if callback==0:
            callback=self.NoOutput()
        self.waitforlock()
        callback(1,'Suspending Virtual Machine %s' % self.vmname)
        if self.suspend() == 0:
            callback(5,'Suspend of %s complete, starting backup' % self.vmname)
            rc=self.backup(archiveformat=archiveformat,destdir=destdir,callback=callback,backupmethod='VMSuspend')
            callback(95,'Resuming Virtual Machine %s' % self.vmname)
            self.resume()
            callback(100,'Backup of %s Complete' % self.vmname)
            self.unlock()
            return rc
        self.unlock()
        return BACKSUSPENDFAIL
    def backup_vmware_snapshot(self,archiveformat='tgz',destdir='',checklock=False, callback=0):
        if callback==0:
            callback=self.NoOutput
        callback(0,'Getting lock')
        self.waitforlock()
        if self.product == 'vmware_server' and self.version < 2:
            self.unlock()
            return BACKMETHODUS
        callback(5,'Generating snapshot')
        if self.takesnapshot() == 0:
            rc=self.backup(archiveformat=archiveformat,destdir=destdir,callback=callback,backupmethod='Snapshot')
            callback(95,'Deleting snapshot')
            self.delsnapshot()
            callback(99,'Unlocking VM')
            self.unlock()
            return rc
        self.unlock()
        return BACKVMSNAPFILE
    def backup_lvm_snapshot(self,archiveformat='tgz',destdir='',checklock=False, callback=0,suspendvm=False):
        if callback==0:
            callback=self.NoOutput
        callback(1,'Getting VM Lock')
        self.waitforlock()
        if self.programs.iscommand('vgdisplay') == False or self.programs.iscommand('lvcreate') == False or self.programs.iscommand('lvremove') == False:
            self.unlock()
            return BACKNOSUPPORT
        line=self.programs.popen('df','-P "%s"' % os.path.dirname(self.configfile)).readlines()[-1].strip()
        device=os.path.dirname(line.split()[0])
        origmount=line.split()[5]
        try:
            VMVG=os.path.basename(line.split()[0]).split('-')[0]
            VMLV=os.path.basename(line.split()[0]).split('-')[1]
        except IndexError:
            self.unlock()
            return BACKLVMSNAPFAIL
        if device == '/dev/mapper':
            line=self.programs.popen('vgdisplay','-c').readlines()[0].strip()
            freepe=int(line.split(':')[15])
            if freepe > VGMINFREEPE:
                if suspendvm:
                    callback(3,'Suspending Virtual Machine')
                    self.suspend()
                callback(5,'Creating LVM Snapshot')
                rc=self.programs.system('lvcreate','> /dev/null 2>&1 -L %s -s -n snap_%s_%d /dev/%s/%s' % (VGSNAPSHOTSIZE,self.vmname,os.getpid(),VMVG,VMLV))
                if rc != 0:
                    if suspendvm:
                        self.resume()
                    self.unlock()
                    return BACKLVMSNAPFAIL
                if suspendvm:
                    callback(8,'Resuming Virtual Machine')
                    self.resume()
                mountpoint=tempfile.mkdtemp()	
                newpath=self.configfile.replace(origmount,mountpoint)
                self.programs.system('mount','/dev/%s/snap_%s_%d %s' % (VMVG,self.vmname,os.getpid(),mountpoint))
                rc=self.backup(archiveformat=archiveformat,lvmconfigpath=newpath,mountpoint=mountpoint,checklock=False,callback=callback,backupmethod='LVMSnapshot')
                callback(95,'Removing LVM Snapshot')
                self.programs.system('umount','%s' % mountpoint)
                self.programs.system('lvremove','> /dev/null 2>&1 -f "/dev/%s/snap_%s_%d"' % (VMVG,self.vmname,os.getpid()))
                os.rmdir(mountpoint)
                callback(99,'Unlocking VM')
                self.unlock()
                return BACKOK
            else:
                self.unlock()
                return BACKNOVGSPACE
        else:
            self.unlock()
            return BACKNOTONLVM
    
def NoOutput(percent,text):
    print '%d percent complete - %s' % (percent,text)
    
class archive:
    def __init__(self,filename='',format=''):
        self.filename=filename
        if format == '':
            if self.filename[-6:] == 'tar.gz' or self.filename[-3:] == 'tgz':
                self.format='tar.gz'
            if self.filename[-7:] == 'tar.bz2' or self.filename[-3:] == 'tbz' or self.filename[-4:] == 'tbz2':
                self.format='tar.bz2'
            if self.filename[-3:] == 'zip':
                self.format='zip'
        else:
            self.format=format
        self.programs=PROGRAMS()
        self.commandlist         = {'tar.gz': ['tar','tzf %s']   ,'tar.bz2': ['tar','tjf %s']   ,'tar': ['tar','tf %s']   ,'unzip': ['-l %s'],'dir':['ls','-1 %s']   }
        self.commandcreate       = {'tar.gz': ['tar','czf %s %s'],'tar.bz2': ['tar','cjf %s %s'],'tar': ['tar','cf %s %s'],'zip': ['%s %s']  ,'dir':['cp','-a %s %s']}
        self.commandextract      = {'tar.gz': ['tar','xzf %s']   ,'tar.bz2': ['tar','xjf %s']   ,'tar': ['tar','xf %s']   ,'unzip': ['%s']   ,'dir':['cp','-a %s %s']}

    def list(self):
        listing=[]
        for line in self.programs.popen(self.commandlist[self.format][0],self.commandlist[self.format][1] % self.filename).readlines():
            listing.append(line.strip())
        return listing
    def extract(self,destdir='.'):
        pass
    def create(self):
        pass
    def append(self):
        pass
    # This is the old self contained restore code.  It needs to be re-written to work generically using the self.commandextract dict above
    def restore(self,source='',dest='/tmp',register=False,callback=NoOutput):
        host=''
        comp=''
        vmxname=''
        cwd=os.getcwd()
        if source[-4:] == '.zip':
            callback(100,'Zip archive restores are not supported yet')
            return UNSUPPORTED
        if source[-3:] == '.gz':
            comp='z'
        if source[-4:] == '.bz2':
            comp='j'
        if dest == '.':
            dest=os.getcwd()
        try:
            temp=source.split(':')
        except AttributeError:
            temp=['',source]
        if len(temp) > 1:
            host=temp[0]
            source=temp[1]
        callback(2,'Scanning archive path depth')
        directory=''
        for line in os.popen('tar -t%sf "%s"' % (comp,source)).readlines():
            if os.path.basename(line.strip())[:14] != 'vmbackup_info.':
                splitpath=os.path.dirname(line.strip()).split('/')
                directory=splitpath[-1]
                pathlen=len(splitpath)
                break
        if directory == '':
            callback(100,'This does not appear to be a VMBackup archive')
            return RESTINVALID
        callback(10,'Restoring archive: %s' % source)
        pid=os.fork()
        if pid == 0:
            os.chdir(dest)
            # First figure out how much path we need to strip out (we only keep the bottom
            # directory)
            if host == '':
                for line in os.popen('tar -xv%sf "%s" -C "%s" --strip %d' % (comp,source,dest,pathlen-1),'r').readlines():
                    if line.strip()[-4:] == '.vmx' or line.strip()[-4:] == '.vdi':
                        vmxname=line.strip()
            else:
                for line in os.popen('ssh %s cat %s|tar -C "%s" -xv%sf - --strip %d' % (host,source,dest,comp,pathlen-1),'r').readlines():
                    if line.strip()[-4:] == '.vmx' or line.strip()[-4:] == '.vdi':
                        vmxname=line.strip()
            os.chdir(cwd)
            # If we are restoring a VMware virtual machine to a system with VirtualBox installed
            # we need to create a VirtualBox configuration file for the Virtual Machine.
            
            if register:
                pass
            os._exit(RESTOK)
        else:
            childpid=0
            dusize=os.path.getsize(source)/1024
            currentsize=0
            if comp == 'z':
                dusize=dusize*2
            if comp == 'j':
                dusize=dusize*3
            while (childpid == 0):
                try:
                    childpid,status=os.waitpid(pid,os.WNOHANG)
                except OSError:
                    childpid=0
                time.sleep(2)
                if host == '':
                    currentsize=long(os.popen('nice du -sk "%s/%s"' % (dest,directory)).readlines()[0].strip().split()[0])
                    percentage=10+int((float(currentsize)/float(dusize)) * 8)
                    callback(percentage,'Restore Running')
                else:
                    callback(50,'Restore to Remote host running')
            callback(100,'Restore completed sucessfully')
            return RESTOK
    def getarchiveinfofilename(self):
        for entry in self.list():
            if len(entry) > 14 and os.path.basename(entry)[:14] == 'vmbackup_info.':
                return(entry)
        return('')
    def getarchiveinfo(self):
        pass

# This function is for backwards compatibility, it has
# been moved to the archive class
def restore(source='',dest='/tmp',register=False,callback=NoOutput):
    myarchive=archive()
    myarchive.restore(source=source,dest=dest,register=False,callback=callback)
