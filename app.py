<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEWCRO_PHP_V7 (WEB VERSION)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .tid-input {
            width: 140px !important;
            max-width: 140px;
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col">

    <!-- Header / Navbar -->
    <header class="bg-slate-900 text-white p-4 shadow-md flex items-center space-x-3">
        <span class="text-2xl font-bold text-amber-400">∞ bgi</span>
        <span class="text-sm tracking-wider text-gray-300 border-l pl-3 border-gray-600">Integrated Cash Solutions</span>
    </header>

    <!-- Sub Header Title -->
    <div class="bg-slate-200 py-2 px-6 text-center text-slate-700 font-semibold text-sm tracking-wide shadow-inner">
        NEWCRO_PHP_V7 (WEB VERSION)
    </div>

    <!-- Main Content Area -->
    <div class="flex-1 flex flex-col md:flex-row p-4 gap-4 max-w-7xl mx-auto w-full">
        
        <!-- Sidebar / User Info Panel -->
        <div class="w-full md:w-80 bg-white p-4 rounded-lg shadow-sm border border-slate-200 flex flex-col justify-between space-y-4">
            <div class="space-y-3">
                <div class="bg-blue-50 border border-blue-200 p-3 rounded text-center">
                    <h2 class="font-bold text-slate-800 text-sm">ADMIN KUNCI</h2>
                    <p class="text-xs text-slate-600">BG BEKASI</p>
                </div>
                
                <div class="text-xs space-y-1.5 text-slate-700 font-mono bg-slate-50 p-3 rounded border border-slate-200">
                    <p>USER ID : 1471191</p>
                    <p>NAMA : ADMIN KUNCI</p>
                    <p>DATE : 22 Aug, 2026</p>
                    <p>LOGIN : 13:45</p>
                </div>
            </div>

            <div class="space-y-2">
                <button class="w-full bg-pink-100 hover:bg-pink-200 text-pink-800 text-xs font-semibold py-2 px-3 rounded border border-pink-300 flex items-center justify-center space-x-1">
                    <span>🌺</span>
                    <span>CETAK KUNCI RPL</span>
                </button>
                <button class="w-full bg-red-50 hover:bg-red-100 text-red-700 text-xs font-semibold py-2 px-3 rounded border border-red-200 flex items-center justify-center space-x-1">
                    <span>🚨</span>
                    <span>Logout</span>
                </button>
            </div>
        </div>

        <!-- Table / Content Panel -->
        <div class="flex-1 bg-white p-4 rounded-lg shadow-sm border border-slate-200 overflow-x-auto">
            <div class="mb-4">
                <button class="bg-slate-700 hover:bg-slate-800 text-white text-xs font-medium py-1.5 px-3 rounded flex items-center space-x-1">
                    <span>➖</span>
                    <span>Kembali ke Daftar Team</span>
                </button>
            </div>

            <!-- Tabel Input TID -->
            <table class="w-full border-collapse border border-slate-300 text-sm">
                <thead>
                    <tr class="bg-emerald-700 text-white">
                        <th class="border border-slate-300 p-2 w-16 text-center">NO</th>
                        <th class="border border-slate-300 p-2 text-left">TID (Bisa Paste Excel di Baris 1)</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Baris 1 sampai 15 (bersih tanpa teks default) -->
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">1</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">2</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">3</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">4</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">5</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">6</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">7</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">8</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">9</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                    <tr>
                        <td class="border border-slate-300 p-2 text-center font-semibold bg-slate-50">10</td>
                        <td class="border border-slate-300 p-2"><input type="text" maxlength="8" class="tid-input border border-slate-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-600"></td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>

</body>
</html>
