<HTML>
	<HEAD><TITLE>test php</TITLE></HEAD>
	<script type='text/javascript'>
		setTimeout(function(){
			//window.location.reload(true);
		}, 2000);
	</script>
	<BODY>
<?php 
	if(($file = fopen("/var/www/html/sensor/log.csv", "r")) !== FALSE)//or die('cannot open file');
	{
		//print 'FILE OPEN';
		print '<table>';
		while(($csv_line = fgetcsv($file, 10240,',')) !== FALSE)
		{
			print '<tr>';
			//print count($csv_line)
			for($idx = 0, $jdx = count($csv_line); $idx < $jdx; $idx++)
			{
				//print $csv_line;
				print '<td>'.$csv_line[$idx].'</td>';

				//print '<td>'.$csv_line[$idx].'</td>';
			}
			//print $csv_line[0];
			print '<td><img src="./images/'.$csv_line[0].'.jpg" height="32" width="32"></td>';
			print '</tr>';
		}
		print '</table>';
		fclose($file) or die('cannot close file');
	}
	else
	{
		print 'FAIL TO OPEN';
	}
?>
		</BODY>
<HTML>
