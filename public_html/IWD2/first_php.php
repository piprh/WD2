<<<<<<< HEAD
<html>
<head>
</head>
<body>
<pre>
<?php
echo "I can make variables and print them to the screen\n";
	echo "Hello world\n";
	$ab = "My test string";
	$ab = "My test string";
	$c = "testing double quotes: $ab\n";
	$d = 'testing single quotes: $ab\n';
echo $c ;
echo $d ;

echo "<b>\n\nPHP is dynamic, so I can tell the time:</b>" ;
$temp = "<br>The current date and time here is:<br>" ;
$now = date('l jS \of F Y h:i:s A') ;
echo "<br>" .$temp.$now." UTC\n" ;
?>
</pre>
</body>
	</html>
<?php
echo <<<_HEAD
	<html>
	<head>
<title>first_php.php</title>
</head>
<body>
_HEAD;
if(isset($_POST['yname'])){
	echo"<p>You typed ",$_POST['yname']," into the box </p>";
	echo 'This is the <a href="first_php.php">link</a> back to the original (same) page';
} else {
	echo <<<_FORM
		<form action="https://en.wikipedia.org/wiki/Special:Random" method="post">
		<pre><font face="arial">
		
Please enter your name:
<input type="text" value="your name" name = "yname"/>
<input type="submit" value="Click me" />
</pre>
</form>
_FORM;
}
echo <<<_TAIL
	</body>
	</html>
	_TAIL;
?>

</body>
</html>



||||||| parent of dc887f4... PH09Feb25 rm secrets
=======
<html>
<head>
</head>
<body>
<?php
echo "Hello world\n";
$ab = "My test string\n";
$ab = 'My test string\n';
$c = "testing double quotes $ab\n";
$d = 'testing single quotes $ab\n';
echo $c;
echo $d;

$temp = "<br/>The current date and time here is:<br/>\n" ;
$now = date('l jS \of F Y h:i:s A') ;
echo "<br/>".$temp.$now." UTC\n" ;

echo <<<_HEAD
	<html>
	<head>
<title>02_my_form_1.php</title>
</head>
<body>
_HEAD;
if(isset($_POST['yname'])){
	echo"<p>You typed ",$_POST['yname']," into the box </p>";
echo 'This is the <a href="02_my_form_1.php">link</a> back to the original (same) page';
} else {
	echo <<<_FORM
		<form action="https://en.wikipedia.org/wiki/Special:Random" method="post">
<pre><font face="arial">

Please enter your name:
<input type="text" value="your name" name = "yname"/>
<input type="submit" value="Click me" />
</pre>
</form>
_FORM;
}
echo <<<_TAIL
	</body>
</html>
_TAIL;

?>

</body>
</html>



>>>>>>> dc887f4... PH09Feb25 rm secrets
