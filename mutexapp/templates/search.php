<?php

function cleanInput($input) {
 
  $search = array(
    '@<script[^>]*?>.*?</script>@si',   // Strip out javascript
    '@<[\/\!]*?[^<>]*?>@si',            // Strip out HTML tags
    '@<style[^>]*?>.*?</style>@siU',    // Strip style tags properly
    '@<![\s\S]*?--[ \t\n\r]*>@'         // Strip multi-line comments
  );
 
    $output = preg_replace($search, '', $input);
    return $output;
  }

function sanitize($input) {
    if (is_array($input)) {
        foreach($input as $var=>$val) {
            $output[$var] = sanitize($val);
        }
    }
    else {
        if (get_magic_quotes_gpc()) {
            $input = stripslashes($input);
        }
        $input  = cleanInput($input);
        $output = preg_replace("/<!--.*?-->/", "", $input);
		$output = preg_replace("/[^a-zA-Z0-9\\\!\-\_\]\[\s\.\{\}\:\#\&\$\*\@\%\^\?\'\;\|\(\)\+]+/", "", html_entity_decode($output, ENT_QUOTES));
    }
    return $output;
}

	try {
		// connect to mongodb
		$m = new Mongo("mongodb://mutexdb:mutexdb@127.0.0.1:27017/mutexdb");
		//echo "Connection to database successfully";
		// select a database
		$db = $m->mutexdb;
		//echo "Database  selected";
		// select the collection
		$collection = $db->mutexs;
		//echo "collection  selected";		
	}
	catch (MongoConnectionException $e) {
		echo $e;
		exit(1);
	}

	$OK = true; // We use this to verify the status of the update.

	$data = '';

	if (isset($_GET['mutex'])) {
		// Create the query
		$data = sanitize($_GET['mutex']);
		$rows = $collection->find(array('mutexsample' => $data));
	}	
	else {
		echo "<strong style='color: red;'>var incorrect!</strong>";
		$m->close();
		exit(1);
	}


	$count = $rows->count();
	$found = 0;
	
	// If there are no records.
	if($count == 0) {
		// do a search on regex column and match the regexs' against string
		$rows = $collection->find();
		foreach ($rows as $document) {
			
			$pattern = '/^('.$document['regex'].')$/i';
			echo $pattern.'<br/>';
			if (preg_match ($pattern, $data, $matches) ) {
				$found = 1;
				break;
			}
			else {
				$found = 0;
			}
		}
		
		if ($found==1) {
			echo $document['comments'];
		}
		else {
			echo "<strong>No match for '{$data}'</strong>";
		}
		
	}
	else {
		/*$res = array();
		while( $rows->hasNext() ) {   
		    $res[] = ($rows->getNext());
		}
		$json_res = json_encode($res);*/
		
		foreach ($rows as $document) {
			echo $document['comments'];
		}
	}
	
	// close the mongo connection
	$m->close();
	
	
	
	
?>
