<?php

session_start();

const USER="ethan";
const PASS="password";

define('SITEURL', "https://devfwd.com/ethan");
define('DOCROOT', $_SERVER['DOCUMENT_ROOT'].'/ethan');

const DB_NAME = 'devfwd_ethan';
const DB_USER = 'devfwd_ethan';
const DB_HOST = 'localhost';
const DB_PASS = 'OM)R!iB~Y)TW';


function login($username, $password) {
//    if ($password === PASS && $username === USER) {
//        $_SESSION['login_times']++;
//        $_SESSION['login'] = true;
//        header('Location: '.SITEURL.'/admin_page/body_admin.php');
//        exit;
//    }
//    else {
//        $_SESSION['message']['error'] = 'inncorect user or password';
//        $_SESSION['incorrect_login_times']++;
//    }
    $username=addslashes($username);
    $sql = "select * from users where username = '".$username."' and password = '".sha1($password)."' limit 1";

    $mysql = db_connect();
    $result = $mysql->query($sql);


    if ($result->num_rows) {
        $row = $result->fetch_object();
        $_SESSION['login_times']++;
        $_SESSION['login'] = $row->id;
        header('Location: '.SITEURL.'/admin_page/body_admin.php');
        exit;
    }
    else {
        $_SESSION['message']['error'] = 'inncorect user or password';
        $_SESSION['incorrect_login_times']++;
    }

}

function check_login() {
    if ($_SESSION['login'] != true) {
        $_SESSION['message']['error'] = 'you must be logged inn to view this page';
        header('location: '.SITEURL.'/login_page/body.php');
        exit;
    }
}

function logout() {
    $_SESSION['login']='notauser';
//    unset($_SESSION['login']);
    $_SESSION['message']['success'] = 'you have logged out';
    header('location: '.SITEURL);
    exit;
}

function db_connect() {
    $mysqli = new mysqli(DB_HOST,DB_USER,DB_PASS,DB_NAME,3306);

    if ($mysqli->connect_errno)
    {
        $_SESSION['message']['error'] = 'could not connect to database';
        return false;
    }
    return $mysqli;
}

function db_query($query) {
    $mysqli = db_connect();
    $mysqli->query($query);
}

?>