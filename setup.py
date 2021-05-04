
bungeeConfig = """
prevent_proxy_connections: false
listeners:
- query_port: 25565
  motd: '&1Another Bungee server'
  tab_list: GLOBAL_PING
  query_enabled: true
  proxy_protocol: false
  ping_passthrough: true
  priorities:
  - survival
  bind_local_address: true
  host: 0.0.0.0:25565
  max_players: 9999
  tab_size: 60
  force_default_server: false
  forced_hosts: {}
remote_ping_cache: -1
network_compression_threshold: 256
permissions:
  default:
  - bungeecord.command.list
  admin:
  - bungeecord.command.server
  - bungeecord.command.alert
  - bungeecord.command.end
  - bungeecord.command.ip
  - bungeecord.command.reload
log_pings: false
connection_throttle_limit: 3
server_connect_timeout: 5000
timeout: 30000
player_limit: -1
ip_forward: true
groups: {}
remote_ping_timeout: 5000
connection_throttle: 4000
log_commands: false
stats: faa1568b-ff7a-46d9-83fa-5d60a4fa3c0d
online_mode: true
forge_support: true
disabled_commands: []
servers:
  survival:
    motd: '&1Just another Waterfall Server'
    address: localhost:8727
    restricted: false

"""
















import os, shutil, itertools, time, threading, jproperties, yaml



dl = True
loop = itertools.cycle(['◔', '◑', '◕', '●', '◕', '◑', '◔', '○'])
def indicator():
    while dl:
        print('\r' + next(loop), end='')
        time.sleep(0.3)
    print('')



print('Run this script in the directory you want to set up the server in. Name your proxy jar to bungee.jar and name the server jar to spigot.jar')
print('Supported proxies: All bungeecord forks')
print('Supported servers: All spigot forks (paper recommended)')

input('Press enter to continue...')

print('Moving files around...')
threading.Thread(target=indicator).start()
os.mkdir('Server')
os.mkdir('Proxy')
os.mkdir('EZplugins')
shutil.copy('spigot.jar','Server/spigot.jar')
shutil.copy('bungee.jar', 'Proxy/bungee.jar')

dl = False

time.sleep(0.4)

print('Files moved around.')


print('Now put your spigot plugins in the EZplugins folder. Press enter to continue')

input('')

os.rename('EZplugins', 'Server/plugins')

print('Now do the same for bungeecord plugins. Press enter to continue')

os.mkdir('EZplugins')

input('')

os.rename('EZplugins', 'Proxy/plugins')

print('Plugins set up. We will now run the server for the first time')

input('Press enter to run the spigot server and set up proxy support')

print('The server will start up in 5 seconds. When you see the message "Done", type stop and then press enter')


dl = True
threading.Thread(target=indicator).start()
time.sleep(5)
dl = False

with open('Server/eula.txt', 'w') as f:
    f.write("eula=true")
os.chdir("Server")
os.system('java -jar spigot.jar nogui')

dl = True
threading.Thread(target=indicator).start()

with open('server.properties', 'r+b') as f:
    p = jproperties.Properties()
    p.load(f)
    p["server-ip"] = "127.0.0.1"
    p["server-port"] = "8727"
    p["query.port"] = "8727"
    p["online-mode"] = "false"
    f.seek(0)
    f.truncate(0)
    p.store(f)
with open('spigot.yml', 'r+') as f:
    y = yaml.load(f.read())
    y["settings"]["bungeecord"] = True
    f.seek(0)
    f.truncate(0)
    yaml.dump(y, f)
with open('bukkit.yml', 'r+') as f:
    y = yaml.load(f.read())
    y["settings"]["connection-throttle"] = -1
    yaml.dump(y, f)

dl = False

print('The proxy will start up in 5 seconds. When you see the prompt, type end and then press enter')
dl = True
threading.Thread(target=indicator).start()
time.sleep(5)
dl = False
os.chdir("../Proxy")
os.system('java -jar bungee.jar')

with open('config.yml', 'w+') as f:
    f.write(bungeeConfig)
os.chdir('../Server')
with open('start.sh', 'w+') as f:
    f.write('''
MaxRam="1024"
MinRam="512"
java -Xmx${MaxRam}M -Xms${MinRam}M -jar spigot.jar nogui
''')

with open('start.bat', 'w+') as f:
    f.write('''
set MaxRam=1024
set MinRam=512
java -Xmx%MaxRam%M -Xms%MinRam%M -jar spigot.jar nogui
''')

os.chdir("../Proxy")
with open('start.sh', 'w+') as f:
    f.write("java -jar bungee.jar")


with open('start.bat', 'w+') as f:
    f.write("java -jar bungee.jar")


print("Start files written, all done!")
