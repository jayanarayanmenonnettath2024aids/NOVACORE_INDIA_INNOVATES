import React from 'react';

const GeographicMap = ({ tickets }) => {
    // Production simulation of a Leaflet/Mapbox integration
    return (
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h2 className="text-lg font-semibold text-gray-900">Regional Issue Heatmap</h2>
                    <p className="text-sm text-gray-500">Live geographic distribution of citizen complaints</p>
                </div>
                <div className="flex items-center space-x-4 text-xs font-semibold">
                    <div className="flex items-center"><span className="w-3 h-3 rounded-full bg-red-500 mr-2"></span> High Density</div>
                    <div className="flex items-center"><span className="w-3 h-3 rounded-full bg-yellow-500 mr-2"></span> Medium</div>
                    <div className="flex items-center"><span className="w-3 h-3 rounded-full bg-blue-500 mr-2"></span> Sparse</div>
                </div>
            </div>

            <div className="relative h-96 w-full bg-slate-100 rounded-lg overflow-hidden border border-slate-200">
                {/* Actual Map Canvas Simulation */}
                <div className="absolute inset-0 opacity-40 grayscale pointer-events-none">
                    <div className="w-full h-full bg-[url('https://api.mapbox.com/styles/v1/mapbox/light-v10/static/77.5946,12.9716,11,0/800x400?access_token=pk.mock')] bg-cover"></div>
                </div>

                {/* Simulated Heatmap Clusters */}
                <div className="absolute top-1/4 left-1/3 w-16 h-16 bg-red-500/30 rounded-full blur-xl animate-pulse"></div>
                <div className="absolute top-1/2 left-1/2 w-24 h-24 bg-red-400/20 rounded-full blur-2xl"></div>
                <div className="absolute bottom-1/3 right-1/4 w-20 h-20 bg-yellow-500/20 rounded-full blur-xl"></div>

                {/* Individual Markers */}
                <div className="absolute top-[40%] left-[45%] group cursor-pointer">
                    <div className="w-3 h-3 bg-red-600 rounded-full border-2 border-white shadow-lg"></div>
                    <div className="hidden group-hover:block absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 bg-gray-900 text-white p-2 rounded text-[10px] shadow-xl z-50">
                        <p className="font-bold">#TKT-9201: Power Failure</p>
                        <p>Sector 4, Main Market Road</p>
                        <p className="text-red-400 mt-1 uppercase font-black">CRITICAL</p>
                    </div>
                </div>

                <div className="absolute bottom-4 right-4 bg-white/90 backdrop-blur p-2 rounded-md shadow-sm border border-gray-200 text-[10px]">
                    <p className="font-bold text-gray-400 uppercase tracking-widest mb-1">Active Filters</p>
                    <div className="flex space-x-2">
                        <span className="bg-indigo-50 text-indigo-600 px-1.5 py-0.5 rounded">All Departments</span>
                        <span className="bg-indigo-50 text-indigo-600 px-1.5 py-0.5 rounded">Last 24 Hours</span>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default GeographicMap;
