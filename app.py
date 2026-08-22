<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEWCRO_PHP_V7 (WEB VERSION)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col">

    <!-- Header / Navbar -->
    <header class="bg-slate-900 text-white p-4 shadow-md flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <span class="text-2xl font-bold text-amber-400">∞ bgi</span>
            <span class="text-sm tracking-wider text-gray-300 border-l pl-3 border-gray-600">Integrated Cash Solutions</span>
        </div>
        <div class="text-sm font-semibold text-gray-300">
            PT. Bringin Gigantara
        </div>
    </header>

    <!-- Sub Header Title -->
    <div class="bg-slate-200 py-2 px-6 text-slate-700 font-semibold text-sm tracking-wide shadow-inner border-b border-slate-300">
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
                    <p>LOGIN : 06:59</p>
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

        <!-- Content Panel: Pilih Team RPL -->
        <div class="flex-1 bg-white p-6 rounded-lg shadow-sm border border-slate-200">
            <h2 class="text-lg font-bold text-slate-800 mb-6 pb-2 border-b border-slate-200">Pilih Team RPL</h2>
            
            <div class="space-y-3 max-w-xl">
                <div class="bg-white border border-slate-300 hover:border-slate-400 p-3 rounded shadow-sm cursor-pointer font-semibold text-slate-700 hover:bg-slate-50 transition">
                    TEAM RPL MALAM 1
                </div>
                <div class="bg-white border border-slate-300 hover:border-slate-400 p-3 rounded shadow-sm cursor-pointer font-semibold text-slate-700 hover:bg-slate-50 transition">
                    TEAM RPL MALAM 2
                </div>
                <div class="bg-white border border-slate-300 hover:border-slate-400 p-3 rounded shadow-sm cursor-pointer font-semibold text-slate-700 hover:bg-slate-50 transition">
                    TEAM RPL PAGI 1
                </div>
                <div class="bg-white border border-slate-300 hover:border-slate-400 p-3 rounded shadow-sm cursor-pointer font-semibold text-slate-700 hover:bg-slate-50 transition">
                    TEAM RPL PAGI 2
                </div>
            </div>
        </div>

    </div>

</body>
</html>
