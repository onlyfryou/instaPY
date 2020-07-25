<?php 
function filterSec($str)
{
    return htmlspecialchars(addslashes(trim($str)));
}

function filterSec2($str)
{
    return addslashes(trim($str));

}

function p($par, $p = false)
{
    if (isset($_POST[$par])) {

        if ($p == false) {
            if (is_array($_POST[$par])) {
                return array_map(function ($item) {
                    return filterSec($item);
                }, $_POST[$par]);
            }

            return filterSec($_POST[$par]);
        } else {
            if (is_array($_POST[$par])) {
                return array_map(function ($item) {
                    return filterSec2($item);
                }, $_POST[$par]);
            }

            return filterSec2($_POST[$par]);
        }

    }
    return false;
}
?>
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kuvarssoft Çekiliş Sc.</title>
</head>
<body>
<?php
   global $subUrl ;
   $subUrl= p('link');
   echo $subUrl."<br>";
   exec("/usr/bin/python3 " . __DIR__ . "/main.py " . $subUrl ,$data);
   
?>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
print_r($data);
//var_dump($data);
 foreach ($data as $key =>$value) {
    $data[$key] = json_decode($value, true);
    //echo $value;
    //echo "<br>";
}
$ArrayLength=count($data);
$min="0";
$sansli=rand($min,$ArrayLength);
echo $sansli;
echo "<br>";
echo "<br>";
//var_dump($data[0]);
//print_r($data[0]["photo"]);
?>
<p><?php print_r($data[$sansli]["username"]);?></p>
<p><?php print_r($data[$sansli]["comment"]);?></p>
<p><?php print_r($data[$sansli]["comment"]);?></p>
<img src="<?php print_r($data[$sansli]["photo"]);?>" alt="" height="42" width="42">
</body>
</html>
