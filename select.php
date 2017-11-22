<?php
    include 'dbconnection.php';
    if($conn)
    {
        //echo "Connection established connection";


        $sql = "SELECT * FROM switch";
        $result = $conn->query($sql);
        if(!empty($result))
        {
            //echo "<pre>";print_r($result);
            while($row = $result->fetch_assoc()) {
                $status = $row["status"];

            }
            echo $status;
        }
        $conn->close();
    }
    


    
?>