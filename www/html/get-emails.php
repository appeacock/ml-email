<?php
//declare(strict_types=1);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require 'shared_functions.php';
include ("static/header.html");
include ("static/sidebar.html");
include ("static/topbar.html");?>
<!-- Start page content -->

<div class="container-fluid">
<h1 class="h3 mb-4 text-gray-800">Emails (<?php echo email_count("INBOX"); ?>)</h1>
<?php display_email_table("INBOX"); ?>
</div>

<!-- End page content -->
<?php include ("static/footer.html");?>