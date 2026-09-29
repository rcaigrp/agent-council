<?php
$results = file_get_contents('results.json');
if ($results) {
    $data = json_decode($results, true);
    echo "<h1>Network Scan Results</h1>";
    echo "<ul>";
    foreach ($data as $result) {
        echo "<li>" . $result . "</li>";
    }
    echo "</ul>";
} else {
    echo "<h2>No scan results available.</h2>";
}
?>