#! /bin/sh
### BEGIN INIT INFO
# Provides:          env-temp.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts/stops temperature monitoring
### END INIT INFO


# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting env-temp.py"
    python3 /usr/local/bin/env-temp.py &
    ;;
  stop)
    echo "Stopping env-temp.py"
    pkill -f /usr/local/bin/env-temp.py
    ;;
  *)
    echo "Usage: /etc/init.d/env-temp.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
