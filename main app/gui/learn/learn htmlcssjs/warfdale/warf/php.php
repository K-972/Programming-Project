<?php


$count = (int)readline('how many terms');

if ($count <= 1) {
    echo 'please enter a posotive number'.PHP_EOL;
    die();
}

$n1 = 0;
$n2 = 1;



for ($i=0; $i < $count; $i++) {
    echo ' '.$n1.PHP_EOL;
    $nterms = $n2 + $n1;
    $n1 = $n2;
    $n2 = $nterms;
}
