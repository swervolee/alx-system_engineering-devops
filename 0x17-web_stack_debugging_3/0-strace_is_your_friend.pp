#Wordpress fix

exec { 'fix-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}
