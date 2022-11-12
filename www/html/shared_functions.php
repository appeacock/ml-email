<?php
declare(strict_types=1);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

function run_($cmd) {
    $command = escapeshellcmd($cmd);
    $result = shell_exec($command);
    return $result;
}

?>