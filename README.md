# Virtual Hosts
#
# Required modules: mod_log_config

# If you want to maintain multiple domains/hostnames on your
# machine you can setup VirtualHost containers for them. Most configurations
# use only name-based virtual hosts so the server doesn't need to worry about
# IP addresses. This is indicated by the asterisks in the directives below.
#
# Please see the documentation at 
# <URL:http://httpd.apache.org/docs/2.4/vhosts/>
# for further details before you try to setup virtual hosts.
#
# You may use the command line option '-S' to verify your virtual host
# configuration.

#
# VirtualHost example:
# Almost any Apache directive may go into a VirtualHost container.
# The first VirtualHost section is used for all requests that do not
# match a ServerName or ServerAlias in any <VirtualHost> block.
#


<VirtualHost *:80>
    ServerAdmin admin@simple-login.com
    DocumentRoot "C:/myprojects/php-login/PhpSimpleLogin"
    ServerName  php-simple-login.loc
	RewriteEngine off
	<Directory "C:/myprojects/php-login/PhpSimpleLogin">
		Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
                DirectoryIndex index.php
		AllowOverride All
	</Directory>
    ErrorLog  "C:/myprojects/php-login/php-simple-login.loc-error.log"
    CustomLog "C:/myprojects/php-login/php-simple-login.loc" common
    <Location />
        RewriteEngine On
        RewriteCond %{REQUEST_FILENAME} -s [OR]
        RewriteCond %{REQUEST_FILENAME} -l [OR]
        RewriteCond %{REQUEST_FILENAME} -d
        RewriteRule ^.*$ - [NC,L]
        RewriteRule ^.*$ /index.php [NC,L]
    </Location>
</VirtualHost>
<VirtualHost *:80>
    ServerAdmin admin@simple-login.com
    DocumentRoot "C:/myprojects/phpSimpleLogin2/PhpSimpleLogin"
    ServerName  php-simple-login2.ps
	RewriteEngine off
	<Directory "C:/myprojects/phpSimpleLogin2/PhpSimpleLogin">
		Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
        DirectoryIndex index.php
		AllowOverride All
	</Directory>
    ErrorLog  "C:/myprojects/phpSimpleLogin2/php-simple-login2.ps-error.log"
    CustomLog "C:/myprojects/phpSimpleLogin2/php-simple-login2.ps" common
    <Location />
        RewriteEngine On
        RewriteCond %{REQUEST_FILENAME} -s [OR]
        RewriteCond %{REQUEST_FILENAME} -l [OR]
        RewriteCond %{REQUEST_FILENAME} -d
        RewriteRule ^.*$ - [NC,L]
        RewriteRule ^.*$ /index.php [NC,L]
    </Location>
</VirtualHost>
<virtualHost *:80>
    serverAdmin admin@php-galary.com
	DocumentRoot "C:/myprojects/php-galary"
	ServerName php-galary.ps
        RewriteEngine off
	<Directory "C:/myprojects/php-galary">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@php-galary.com
	DocumentRoot "C:/myprojects/ajax"
	ServerName php-ajax.ps
        RewriteEngine off
	<Directory "C:/myprojects/ajax>
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@log_in.com
	DocumentRoot "C:/myprojects/log_in/login"
	ServerName login-facebook.ps
        RewriteEngine off
	<Directory "C:/myprojects/log_in/login">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/log_in/login.ps-error.log"
     CustomLog "C:/myprojects/log_in/login-facebook.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@login_nodejs.com
	DocumentRoot "C:/myprojects/log_in/login_nodejs"
	ServerName login-nodejs.ps
        RewriteEngine off
	<Directory "C:/myprojects/log_in/login_nodejs">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/log_in/login_nodejs.ps-error.log"
     CustomLog "C:/myprojects/log_in/login-nodejs.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@facebook-login.com
	DocumentRoot "C:/myprojects/facebook/login-facebook"
	ServerName facebook-login.ps
        RewriteEngine off
	<Directory "C:/myprojects/facebook/login-facebook">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/facebook/facebook-login.ps-error.log"
     CustomLog "C:/myprojects/facebook/facebook-login.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@diana-app.com
	DocumentRoot "C:/myprojects/diana/smart-mirro"
	ServerName diana-app.ps
        RewriteEngine off
	<Directory "C:/myprojects/diana/smart-mirro">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/diana/diana-app.ps-error.log"
     CustomLog "C:/myprojects/diana/diana-app.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@login-in-facebook.com
	DocumentRoot "C:/myprojects/login_face/nodejs"
	ServerName  login-in-facebook.ps
        RewriteEngine off
	<Directory "C:/myprojects/login_face/nodejs">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/login_face/login-in-facebook.ps-error.log"
     CustomLog "C:/myprojects/login_face/login-in-facebook.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@apijility.com
	DocumentRoot "C:/myprojects/apps/apigility"
	ServerName  apijility.ps
        RewriteEngine off
	<Directory "C:/myprojects/apps/apigility">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/apps/apijility.ps-error.log"
     CustomLog "C:/myprojects/apps/apijility.ps" common
</virtualHost>
<virtualHost *:80>
    serverAdmin admin@laravel.com
	DocumentRoot "C:/myprojects/laravel/apps"
	ServerName  laravel.ps
        RewriteEngine off
	<Directory "C:/myprojects/laravel/apps">
	    Order deny,allow
		Deny from all
		Allow from 127.0.0.1
		Require all granted
		#DirectoryIndex index.php
		AllowOverride All
	</Directory>
	 ErrorLog  "C:/myprojects/laravel/laravel.ps-error.log"
     CustomLog "C:/myprojects/laravel/laravel.ps" common
</virtualHost>
