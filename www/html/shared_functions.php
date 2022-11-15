<?php
declare(strict_types=1);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

function email_count($mailbox) {
    $result = exec('python3 /home/email/ml-email/python/get_email_count.py ' . $mailbox);
    return trim($result);
}

function display_email_table($mailbox) {
    $result = json_decode(exec('python3 /home/email/ml-email/python/get_emails.py ' . $mailbox), true);
    $emails = array_keys(array_reverse($result));
    echo <<< EOT
    <div class="table-responsive">
        <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
        <thead>
            <tr>
                <th><input type='checkbox' id='allid' onclick='toggle(this)'></th>
                <th>Date</th>
                <th>Name</th>
                <th>Address</th>
                <th>Subject</th>
            </tr>
        </thead>
        <tbody>
    EOT;
    for($id = 1; $id < count($result); $id++) {
        echo "<tr><td><input type='checkbox' id='id" . $result[$emails[$id]][0] . "' name='get_emails'>";
        echo "<td>" . $result[$emails[$id]][5];
        echo "<td>" . $result[$emails[$id]][1];
        echo "<td>" . $result[$emails[$id]][2];
        echo "<td>" . $result[$emails[$id]][6] . "</tr>";
    }
    echo <<< EOT
            </tbody>
        </table>
    </div>
    EOT;
}
?>