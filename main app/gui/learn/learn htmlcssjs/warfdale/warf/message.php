<?php



if ($_SESSION['message']) {

    echo ($_SESSION['message']['error'] ? "<div class='message error'>".$_SESSION['message']['error']."</div>" : '');
    echo ($_SESSION['message']['success'] ? "<div class='message success'>".$_SESSION['message']['success']."</div>" : '');

    unset($_SESSION['message']);

}

