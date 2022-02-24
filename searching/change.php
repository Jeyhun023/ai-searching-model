$files = scandir('data/');

foreach($files as $file) {
  echo $file;
}