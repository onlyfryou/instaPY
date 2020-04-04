<?php
function fail($o)
{
	echo 'Fail:<br>';
	echo json_encode($o);
	exit(0);
}


$subUrl = 'B-NO0LJnKmG/';

try
{
	$data = [];
	$cmd="C:\\wamp64\\www\\main.py";
	$python="C:\\Users\\oguzh\\AppData\\Local\\Microsoft\\WindowsApps\\python3.exe";
	exec('$python $cmd' . $subUrl ,$data);
	var_dump($data);die();
	$output = json_decode($data);
	
	if($data['status'] != 'OK')
		fail($data);
	
	foreach($output['data'] as $userData)
	{
		echo $userData['username'] . ':' . $userData['comment'] . '<br>';
	}
}
catch(Exception $e)
{
	fail($e);
}