# secure-nginx

This repo shows examples of nginx settings for tls connection, redirect http to https connection
and so on.

1. Add instruction for tls settings (generate and install certificates)
2. Add target service (python api for instance)
3. Add redirect http to https

### Part 1

It is often necessary to organize the operation of some web service with encryption support, but there is no need for a valid (paid) SSL certificate. For example, organize access to the server control panel for your own needs or the needs of the company (without public access).

Here we briefly describe how you can quickly generate a self-signed SSL certificate for nginx if you don’t have one after installing the web server from packages (rpm, deb).

Step 1 (generate certificate):
```bash
mkdir /etc/nginx/ssl
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
```

When you run the second command, you will need to fill out several fields. Here we will give an example when you have to generate a certificate without specifying the organization:

```
Country Name (2 letter code) [AU]:RU
State or Province Name (full name) [Some-State]:Krasnodarskiy kray
Locality Name (eg, city) []:Krasnodar 
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Private
Organizational Unit Name (eg, section) []:Private
Common Name (e.g. server FQDN or YOUR name) []:your_domain.com
Email Address []:admin@your_domain.com
```

Step 2 (setup certificate):
```bash
server {
        ...
        ssl_certificate /etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /etc/nginx/ssl/nginx.key;
        ...
}
```
See nginx.conf file for more information.

Step 3 (check configuration and apply settings):

```bash
# launch configuration checking by nginx internal mechanism
nginx -t
# check, that test is successful and apply changes
service nginx reload
```
