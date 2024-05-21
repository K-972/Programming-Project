<?php

include '../config.php';

check_login();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    print_r($_POST);
    print_r($_FILES);
    exit;
}

include DOCROOT.'/admin_page/metahead_admin.php';
include DOCROOT.'/admin_page/header_admin.php';

?>
<div class="row">
    <div class="col-3">
        <div>
            you are logged in as an admin
        </div>
    </div>
    <div class="col-4 offset-6">
        <a class="btn-primary btn" aria-current="page" href='../logout.php'>logout</a>
    </div>
</div>


<form enctype="multipart/form-data" method="post">
    <?php
    $mysql = db_connect();
    if (isset($error)){

        echo ('<strong>'.$error.'</strong>');

    }

    ?>
    <label class="form-label" for="customFile">input yur file here</label>
    <input type="file" class="form-control" id="customFile" />
    <div class="input-group mb-3">
        <span class="input-group-text" id="name_input">input name</span>
        <input name="input_name" type="text" class="form-control" placeholder="enter name of your file" aria-label="name" aria-describedby="basic-addon1" value="<?php echo ($_POST['input_name']? $_POST['input_name'] : '') ?>">
    </div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
            <label class="input-group-text" for="inputGroupSelect01">Options</label>
        </div>
        <select name="category" class="custom-select" id="inputGroupSelect01">
            <option value="">Choose...</option>
                <?php
                $sql = "select * from categories";
                $result = $mysql->query($sql);
                if ($result->num_rows) {
                    while ($row = mysqli_fetch_object($result)) {
                        echo('<option '.($_POST['category'] == $row->id ? 'selected="selected"' : '').' value="' . $row->id . '">' . $row->name . '</option>');
                    }
                }
                ?>
        </select>
    </div>
    <input class="btn btn-primary" type="submit" value="Submit">

</form>

<?php

// connect to database

//prepare the sql query
    $sql = "select * from homework";
//run the sql query
    $result = $mysql->query($sql);
//check if query has results
    if ($result->num_rows) {
        //query has results, echo header
        echo '<table class="table">';
            echo '<thead>';
                echo '<tr>';
                    echo '<th>ID</th>';
                    echo '<th>Name</th>';
                    echo '<th>Category</th>';
                echo '</tr>';
            echo '</thead>';
        //query has results loop information
            echo '<tbody>';

                while ($row = mysqli_fetch_object($result)) {

                    echo '<tr>';
                        echo '<td>'.$row->id.'</td>';
                        echo '<td>'.$row->name.'</td>';
                        echo '<td>'.$row->category_id.'</td>';
                    echo '</tr>';

                }

            echo '</tbody>';
        echo '</table>';

    }
    else {
        //query has no results
        echo ('no results');
    }




include DOCROOT.'/admin_page/footer_admin.php';

?>


