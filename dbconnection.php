<?php
    $servername = "52.172.191.222";
    $username = "3x3conect";
    $password = "@3CDt1vk11tn43CT";
    $dbname = "technofarm";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    //echo "Connected successfully";
?>