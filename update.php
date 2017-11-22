<?php
    include 'dbconnection.php';

    $status= $_GET["id"];
    //echo $id;
    if($conn)
    {   
       
       /* $sql = "UPDATE switch SET status=".$id." WHERE id=1";

        if ($conn->query($sql) === TRUE) {
            echo "Record updated successfully";
        } else {
            echo "Error updating record: " . $conn->error;
        }*/
        echo $status;
        $updateSql = "UPDATE switch SET status=".$status." WHERE id=1";
        $conn->query($updateSql);

        $conn->close();
    }
?>