<?php

class UserController {

    public function login() {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // ❌ SQL Injection vulnerability
        $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
        $result = mysqli_query($this->db, $query);

        if ($result) {
            echo "Login successful";
        } else {
            echo "Login failed";
        }
    }

    public function calculateDiscount($amount) {
        // ❌ Assignment instead of comparison
        if ($amount = 100) {
            return $amount * 0.10;
        }

        return 0;
    }

    public function
