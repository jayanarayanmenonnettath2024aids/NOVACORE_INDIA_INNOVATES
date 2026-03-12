import React, { useState } from 'react';
import GeographicMap from '../components/GeographicMap';

const RegionalMapPage = () => {
    const [selectedZone, setSelectedZone] = useState('All Bengaluru');

    return (
        <div className="max-w-7xl mx-auto py-8 px-4">
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-3xl font-black text-slate-900 tracking-tight">Geographic Grievance Map</h1>
                    <p className="text-slate-500 mt-2">Spatial distribution of infrastructure issues across the city.</p>
                </div>
                <div className="flex space-x-2">
                    {['North', 'South', 'East', 'West', 'Central'].map(zone => (
                        <button
                            key={zone}
                            onClick={() => setSelectedZone(zone)}
                            className={`px-4 py-2 rounded-xl text-sm font-bold transition-all ${selectedZone === zone ? 'bg-indigo-600 text-white shadow-lg' : 'bg-white text-slate-600 hover:bg-slate-50'
                                }`}
                        >
                            {zone}
                        </button>
                    ))}
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div className="lg:col-span-2">
                    <GeographicMap />
                </div>
                <div className="space-y-6">
                    <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
                        <h3 className="font-bold text-slate-900 mb-4">Hotspot Analysis</h3>
                        <div className="space-y-4">
                            {[
                                { area: 'MG Road Junction', issues: 12, type: 'Water', status: 'High' },
                                { area: 'Sector 7 Park', issues: 8, type: 'Sanitation', status: 'Medium' },
                                { area: 'Airport Terminal 2', issues: 5, type: 'Electricity', status: 'Low' },
                                { area: 'South Plaza', issues: 15, type: 'Roads', status: 'High' },
                            ].map((hotspot, i) => (
                                <div key={i} className="flex items-center justify-between p-3 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                                    <div>
                                        <p className="text-sm font-bold text-slate-900">{hotspot.area}</p>
                                        <p className="text-[10px] text-slate-400 uppercase font-bold tracking-widest">{hotspot.type}</p>
                                    </div>
                                    <div className="text-right">
                                        <p className="text-sm font-black text-indigo-600">{hotspot.issues} Cases</p>
                                        <span className={`text-[8px] font-black uppercase ${hotspot.status === 'High' ? 'text-red-500' : 'text-slate-400'}`}>
                                            {hotspot.status} Density
                                        </span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    <div className="bg-indigo-600 p-6 rounded-2xl text-white shadow-xl shadow-indigo-500/20">
                        <h3 className="font-bold text-lg mb-2">Predictive Logic</h3>
                        <p className="text-indigo-100 text-sm leading-relaxed">
                            AI models predict a potential <span className="font-bold text-white uppercase">Power Outage</span> in the North-West quadrant due to overlapping citizen reports of voltage spikes.
                        </p>
                        <button className="mt-4 w-full py-2 bg-white text-indigo-600 rounded-xl text-xs font-bold uppercase tracking-widest hover:bg-indigo-50 transition-all">
                            Dispatch Preventive Crew
                        </button>
                    </div>
                </div>
            </div>

            <div className="mt-8 bg-white p-8 rounded-2xl border border-slate-100">
                <h3 className="font-bold text-slate-900 mb-6">Zone Comparison Analytics</h3>
                <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                    {['North', 'South', 'East', 'West', 'Central'].map(zone => (
                        <div key={zone} className="text-center">
                            <div className="h-24 w-full bg-slate-50 rounded-xl mb-3 flex items-end p-2">
                                <div className="bg-indigo-400 w-full rounded-lg" style={{ height: `${Math.random() * 80 + 20}%` }}></div>
                            </div>
                            <p className="text-xs font-bold text-slate-400 uppercase tracking-tighter">{zone}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default RegionalMapPage;
