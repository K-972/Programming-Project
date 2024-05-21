<?php

include '../config.php';




if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = htmlspecialchars($_POST["username"]);
    $password = htmlspecialchars($_POST["password"]);

    login($username, $password);

}



include '../login_page/metahead_login.php';
include '../login_page/header_login.php';


echo 'We have logged in '.intval($_SESSION['login_times']).' times'.PHP_EOL;
echo 'We have failed to log in '.intval($_SESSION['incorrect_login_times']).' times';

include DOCROOT.'/message.php';

?>
<form method="post">
    <?php
    if (isset($error)){

        echo ('<strong>'.$error.'</strong>');

    }
    ?>
    <div class="input-group mb-3">
        <span class="input-group-text" id="username_input">username</span>
        <input name="username" type="text" class="form-control" placeholder="enter your username" aria-label="username" aria-describedby="basic-addon1" value="<?php echo ($username); ?>">
    </div>

    <div class="input-group mb-3">
        <span class="input-group-text" id="password_input">password</span>
        <input name="password" type="password" class="form-control" placeholder="enter your password" aria-label="password" aria-describedby="basic-addon1">
    </div>
    <input class="btn btn-primary" type="submit" value="Submit">

</form>



<?php

include '../login_page/footer_login.php';


?>