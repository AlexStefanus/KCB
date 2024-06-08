<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find Your Keyboard</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap">
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            height: 100vh;
            margin: 0;
            padding-left: 20px;
            font-family: 'Poppins', sans-serif;
            background-image: url('now.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: #009eff; /* Warna teks menjadi biru dengan kode #009eff */
        }
        .container {
            text-align: left;
        }
        .small-text {
            font-size: 24px;
            letter-spacing: 2px;
            margin: -10px 0 0 0; /* Menggeser ke atas sebanyak -10px */
            padding: 5px 0 0 0;
        }
        .big-text {
            font-size: 72px;
            letter-spacing: 3px;
            margin: 0;
            padding: 0;
            font-weight: 700;
        }
        .button {
            background-color: white;
            border: 2px solid #009eff; /* Warna border tombol */
            color: #009eff; /* Warna teks tombol */
            font-size: 24px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 50px; /* Membuat tombol berbentuk oval panjang */
            margin-top: 20px; /* Menambahkan jarak antara teks dan tombol */
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }
        .button:hover {
            background-color: #009eff; /* Warna latar belakang tombol saat dihover */
            color: white; /* Warna teks tombol saat dihover */
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="small-text"><?php echo 'FIND YOUR'; ?></div>
        <div class="big-text"><?php echo 'KEYBOARD'; ?></div>
        <button class="button">MULAI CARI!</button>
    </div>
</body>
</html>
