<?php
$conn=new PDO("mysql:host=localhost;dbname=clinic", "root", "" );
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
if($_GET['action']=='insert')
{
$sql="INSERT INTO patient (name,address,phone,blood_group) 
VALUES ('$_POST[name]','$_POST[address]','$_POST[phone]','$_POST[blood_group]')";
$conn->exec($sql);
}
else if($_GET['action']=='view')
{
$sql1= "SELECT * FROM patient";
$result = $conn->prepare($sql1); 
$result->execute();
$result->setFetchMode(PDO::FETCH_ASSOC);
$res= $result->fetchAll();
echo json_encode($res);
}
else if($_GET['action']=='load')
{
$sql2="SELECT pat_id,name,address,phone,blood_group FROM patient WHERE pat_id=".$_GET['pat_id'];
$result1 = $conn->prepare($sql2); 
$result1->execute();
$result1->setFetchMode(PDO::FETCH_ASSOC);
$res1= $result1->fetchAll();
echo json_encode($res1);
}
else if($_GET['action']=='edit')
{
$sql3="UPDATE patient SET name='$_POST[name]', address='$_POST[address]', phone='$_POST[phone]', blood_group='$_POST[blood_group]' WHERE pat_id=".$_GET['pat_id'];
$conn->exec($sql3);
}
else if($_GET['action']=='del')
{
$sql4="DELETE FROM patient WHERE pat_id=".$_GET['pat_id'];
$conn->exec($sql4);
}
?>