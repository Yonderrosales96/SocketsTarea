require "socket"
class Server
  def initialize( port, ip )
    @server = TCPServer.open( ip, port )
    @connections = Hash.new
    @clients = Hash.new
    @connections[:clients] = @clients
    puts "Servidor Inicializado"
    run
  end

  def run
    loop {
      Thread.start(@server.accept) do | client |
        nick_name = client.gets.chomp.to_sym
        @connections[:clients].each do |other_name, other_client|
          puts "other name : #{other_name} y other_client : #{other_client}"
          if nick_name == other_name || client == other_client
            client.puts "Nombre de usuario ya existe"
            Thread.kill self
          end
        end
        puts "#{nick_name} #{client}"
        @connections[:clients][nick_name] = client
        client.puts "Se ha establecido la coneccion, Bienvenido"
        listen_user_messages( nick_name, client )
      end
    }.join
  end

  def listen_user_messages( username, client )
    loop {
      msg = client.gets.chomp
      @connections[:clients].each do |other_name, other_client|
        unless other_name == username
          other_client.puts "#{username.to_s}: #{msg}"
        end
      end
    }
  end
end
puts "Inicializando Servidor"
puts "Ingrese direccion IP"
ip = $stdin.gets.chomp
Server.new( 3000, ip )
