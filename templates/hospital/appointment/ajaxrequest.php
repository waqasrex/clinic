<?php
$conn=new PDO("mysql:host=localhost;dbname=clinic", "root", "" );
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
header('Content-Type: application/json');
if ($_GET['action']=='search')
{
        $resp = new stdClass;
  try{
        $sql="SELECT * FROM patient WHERE phone=".$_GET['phone']; 
        $result = $conn->prepare($sql); 
        $result->execute();
        $result->setFetchMode(PDO::FETCH_ASSOC);
        $res= $result->fetchAll();
    if(count($res)==0){
            $resp->result=0;
            $resp->data = null;
            $resp->message = 'Empty Response';
                          }
    else{
        $resp->result=1;
        $resp->data = $res[0];
        $resp->message = 'Success, and data retrived';
            }
        }
  catch(Exception $e){
        $resp->result=-1;
        $resp->data = null;
        $resp->message = $e->getMessage();
                        }
        echo json_encode($resp);
}
else if ($_GET['action']=='submit')
{       $respo = new stdClass;
  try{
    if($_GET['pat_id']==""){
        $sql3="INSERT INTO patient (name,address,phone,blood_group)
        VALUES ('$_POST[name]','$_POST[address]','$_POST[phone]','$_POST[blood_group]')";
        $conn->exec($sql3);
        $id = $conn->lastInsertId();
        $sql4="INSERT INTO patient_visit (pat_id,doc_id,category,time,date)
        VALUES ('$id','$_POST[doc_id]','$_POST[category]','$_POST[time]','$_POST[date]')";
        $conn->exec($sql4);}
    else{
        $sql8="INSERT INTO patient_visit (pat_id,doc_id,category,time,date)
        VALUES ('$_POST[pat_id]','$_POST[doc_id]','$_POST[category]','$_POST[time]','$_POST[date]')";
        $conn->exec($sql8);}
        $respo->result=1;
        $respo->date="";
        $respo->message="ok";
    }
  catch(Exception $e){
        $respo->result=-1;
        $respo->date=null;
        $respo->message=$e->getMessage();
  }      
        echo json_encode($respo);
}
else if ($_GET['action']=='view')
{
        $sql5= "SELECT * FROM patient_visit";
        $result = $conn->prepare($sql5); 
        $result->execute();
        $result->setFetchMode(PDO::FETCH_ASSOC);
        $res= $result->fetchAll();
        echo json_encode($res);
}
else if($_GET['action']=='load')
{
        $sql6="SELECT vis_ID,pat_id,doc_id,category,time,date FROM patient_visit WHERE vis_ID=".$_GET['vis_ID'];
        $result1 = $conn->prepare($sql6); 
        $result1->execute();
        $result1->setFetchMode(PDO::FETCH_ASSOC);
        $res1= $result1->fetchAll();
        echo json_encode($res1);
}
else if($_GET['action']=='edit')
{
        $sql7="UPDATE patient_visit SET pat_id='$_POST[pat_id]', doc_id='$_POST[doc_id]', category='$_POST[category]', time='$_POST[time]', date='$_POST[date]' WHERE vis_ID=".$_GET['vis_ID'];
        $conn->exec($sql7);
}
else if($_GET['action']=='del')
{
        $sql8="DELETE FROM patient_visit WHERE vis_ID=".$_GET['vis_ID'];
        $conn->exec($sql8);
}
?>