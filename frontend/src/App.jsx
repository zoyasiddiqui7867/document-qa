function App() {
  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-50 p-8 flex flex-col items-center justify-center">
      
      {/* 1. Main Container with v4 Shadow and Border */}
      <div className="max-w-md w-full bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-2xl">
        
        {/* 2. Header with Gradient Text */}
        <h1 className="text-2xl font-bold bg-linear-to-r from-sky-400 to-emerald-400 bg-clip-text text-transparent">
          Document Q&A System
        </h1>
        
        <p className="mt-2 text-zinc-400 text-sm">
          Local RAG Analysis Engine initialized.
        </p>

        {/* 3. Testing Interactivity & v4 Hover Effects */}
        <div className="mt-6 space-y-4">
          <div className="group p-4 bg-zinc-800/50 rounded-xl border border-transparent hover:border-sky-500/50 hover:bg-zinc-800 transition-all cursor-pointer">
            <span className="text-sky-400 font-semibold group-hover:text-sky-300">
              Check Upload Status
            </span>
            <p className="text-xs text-zinc-500 mt-1">Verify if the local PDF parser is ready.</p>
          </div>

          {/* 4. A "Processing" Pulse Animation */}
          <div className="flex items-center gap-3 p-3 bg-emerald-500/10 rounded-lg">
            <div className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
            </div>
            <span className="text-xs font-medium text-emerald-400 uppercase tracking-wider">
              Backend Online (Local)
            </span>
          </div>
        </div>

        {/* 5. Testing Grid Layout */}
        <div className="mt-8 grid grid-cols-2 gap-4">
          <button className="py-2 px-4 bg-zinc-100 text-zinc-900 font-bold rounded-lg hover:bg-white active:scale-95 transition-transform">
            Upload PDF
          </button>
          <button className="py-2 px-4 bg-zinc-800 text-zinc-300 font-bold rounded-lg border border-zinc-700 hover:bg-zinc-700">
            Ask Question
          </button>
        </div>
        
      </div>
      
      <footer className="mt-8 text-zinc-600 text-xs font-mono">
        Tailwind v4 + React Compiler Active
      </footer>
    </div>
  );
}

export default App;