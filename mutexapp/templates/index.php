<?php

function validate_ip($ip)
{
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) === false) {
        return false;
    }
    return true;
}

function get_client_ip() {
    $ip_keys = array('HTTP_CLIENT_IP', 'HTTP_X_FORWARDED_FOR', 'HTTP_X_FORWARDED', 'HTTP_X_CLUSTER_CLIENT_IP', 'HTTP_FORWARDED_FOR', 'HTTP_FORWARDED', 'REMOTE_ADDR');
    foreach ($ip_keys as $key) {
        if (array_key_exists($key, $_SERVER) === true) {
            foreach (explode(',', $_SERVER[$key]) as $ip) {
                // trim for safety measures
                $ip = trim($ip);
                // attempt to validate IP
                if (validate_ip($ip)) {
                    return $ip;
                }
            }
        }
    }
 
    return isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : false;
}

function log_write($text, $filename) {
	if (!file_exists($filename)) { touch($filename); chmod($filename, 0666); }
	clearstatcache();
	// 10MB file
	if (filesize($filename) > 10*1024*1024) {
		$filename2 = "$filename.old";
		if (file_exists($filename2)) unlink($filename2);
		rename($filename, $filename2);
		touch($filename); chmod($filename, 0666);
	}
	file_put_contents($filename, $text, FILE_APPEND | LOCK_EX);
	//fclose($filename);
}

$rem_ip = get_client_ip();
$ua = $_SERVER["HTTP_USER_AGENT"];
$referer = $_SERVER["HTTP_REFERER"];
$log_file = '/opt/mutexdb/logs/'. date("Ymd") .'_visitors.txt';
$date = date('d-m-Y H:i:s');
$t = $date.','.$rem_ip.','.$referer.','.$ua.",\r\n";
log_write($t, $log_file);

include("header.php"); 
?>
	  
	  <!-- Begin page content -->
	  <div class="container">
	    <!--<div class="page-header">
	      
	    </div> //-->
	    
	<div class="container">
	<br/>&nbsp;<br/><br/>&nbsp;<br/>
	<ul class="nav nav-tabs col-centered" id="theTabs">
		<li class="active"><a href="#search">Search</a></li>
	</ul>
	 
	<div class="tab-content">
		<div class="tab-pane active" id="search">
			<br/>&nbsp;<br/>
			<div style="text-align:center;">
				<form class="form-horizontal form1" role="form" method="get">				<div class="form-group">							<div class="input-group col-sm-6 col-centered">
						<input id="mutex" name="mutex" type="text" class="form-control" placeholder="Paste that mutex..." />						<span class="input-group-btn">
							<button type="button" class="btn btn-default btnSearchByName">
							<span class="glyphicon glyphicon-search"> Search</span>
							</button>
						</span>
					</div>
				</div>
   				</form>
				
				<div class="row notificationPanel">
			        <div class="col-sm-2"></div>
		            <div class="col-sm-8  alert alert-warning" role="alert">
						<p></p>
					</div>
				</div>
				<div class="row">
					<div class="col-sm-2" style="text-align: center;"></div>
					<div class="col-sm-8" style="text-align: center;">
						<div id="result" style="text-align: center;">
						</div>
					</div>
				</div>
				


			</div>
			
			<p><br/>&nbsp;<br/>Got a Mutex to verify, no problem; paste it up here and we will check it for you. <br/>This is a <strong>BETA</strong> service and we will continue to improve our service.<br/><br/><div class="social-likes" data-url="http://www.mutexdb.com" data-title="MutexDB">
				<div class="facebook" title="Share link on Facebook">Facebook</div>
				<div class="twitter" title="Share link on Twitter">Twitter</div>
				<div class="plusone" title="Share link on Google+">Google+</div>
			</div></p>
		</div>
		<!-- End of search tab //-->
	</div>
	</div>

	    
	  </div>
	</div>

	<?php
	/*  Footer Script  */
	include("footer.php");
	?>
	
	<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
	<script src="assets/js/bootstrap.min.js"></script>
	<script src="assets/js/social.js"></script>
	<script type="text/javascript">
	
		$('#theTabs a').click(function (e) {
			 e.preventDefault();
			 $(this).tab('show');
		});

		$(function () {
			$('#myTab a:last').tab('show');
		})
		
		jQuery(document).ready(function ($) {
			$('#tabs').tab();
		});

		jQuery(document).ready(function($) {
			$('.btnSearchByName').click(function(){
		    if (!validateData($('input#mutex').val())) {
		    	showErrorPanel("Paste that Mutex to search...");
		        return false;
		    }
		    makeAjaxRequest("mutex");
		});

		$('.form1').submit(function(e){
			e.preventDefault();
		    if (!validateData($('input#mutex').val())) {
		    	showErrorPanel("Paste that Mutex to get results!");
		        return false;
		 	}
		 	validateData()
		    makeAjaxRequest("mutex");
		    return false;
		});

		function makeAjaxRequest(type) {
			
			if (type == "mutex") {
				$("#result").html("<img alt='finding' src='assets/img/loader.gif'/>");
		        $.ajax({url: 'assets/find.php',
		         	type: 'post',
		            data: {mutex: $('input#mutex').val()},
		            success: function(response) {
						$('#result').html(response);
		             }
		           });
		      } 
		 }
		
		function validateData(data) {
			if (data == "") {
		    	return false;
		    } else {
		    	return true;
		     }
		}
		
		function showErrorPanel(msg) {
			$('.notificationPanel div:eq(1)').text(msg).wrap("<strong></strong>");
		    $('.notificationPanel').slideDown('normal');
		    setTimeout(function() {
		    	$('.notificationPanel').slideUp('normal');
		    }, 3500)
		}
	  });
	
	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

	  ga('create', 'UA-328519-11', 'auto');
	  ga('send', 'pageview');
	</script>

   </body>
</html>
