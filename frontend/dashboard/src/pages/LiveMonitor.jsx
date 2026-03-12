import React, { useState, useEffect } from 'react';
import { useAppState } from '../context/AppStateContext';

const LiveMonitor = () => {
    const [activeCalls, setActiveCalls] = useState([]);

    // Simulate live calls arriving via WebSockets
    useEffect(() => {
        const interval = setInterval(() => {
            const newCall = {
                id: Math.random().toString(36).substr(2, 9),
                phone: `+9198765${Math.floor(Math.random() * 90000) + 10000}`,
                status: 'Ongoing',
                startTime: new Date().toLocaleTimeString(),
                duration: '0:01',
                analysing: Math.random() > 0.5
            };
            setActiveCalls(prev => [newCall, ...prev].slice(0, 8));
        }, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="max-w-7xl mx-auto py-8 px-4">
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-3xl font-bold text-gray-900">AI Live Monitor</h1>
                    <p className="text-gray-500 mt-1">Real-time surveillance of incoming citizen calls</p>
                </div>
                <div className="flex items-center space-x-2">
                    <span className="flex h-3 w-3 relative">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
                    </span>
                    <span className="text-sm font-semibold text-red-600 uppercase tracking-widest">Live Transcribing</span>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {activeCalls.map((call) => (
                    <div key={call.id} className="bg-white rounded-xl shadow-lg border-2 border-indigo-50 p-6 flex flex-col h-64 overflow-hidden transform transition hover:scale-105">
                        <div className="flex justify-between items-start mb-4">
                            <div>
                                <p className="text-xs font-bold text-indigo-500 uppercase tracking-widest">Call ID: {call.id}</p>
                                <h3 className="text-lg font-bold text-gray-900 mt-1">{call.phone}</h3>
                            </div>
                            <span className="bg-green-100 text-green-700 px-2 py-1 rounded-md text-[10px] font-bold">ACTIVE</span>
                        </div>

                        <div className="flex-grow">
                            <div className="flex items-center space-x-2 mb-3">
                                <div className="flex-grow h-1 bg-gray-100 rounded-full overflow-hidden">
                                    <div className="h-full bg-indigo-500 w-1/3 animate-pulse"></div>
                                </div>
                                <span className="text-[10px] text-gray-400 font-mono">{call.duration}</span>
                            </div>

                            <div className="space-y-2">
                                <p className="text-sm text-gray-700 italic">"I'm calling from Sector 7, there's a problem with..."</p>
                                {call.analysing && (
                                    <div className="flex items-center space-x-2">
                                        <div className="flex space-x-1">
                                            <div className="h-1.5 w-1.5 bg-indigo-400 rounded-full animate-bounce"></div>
                                            <div className="h-1.5 w-1.5 bg-indigo-400 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                                            <div className="h-1.5 w-1.5 bg-indigo-400 rounded-full animate-bounce [animation-delay:-0.5s]"></div>
                                        </div>
                                        <span className="text-[10px] font-bold text-indigo-400 uppercase tracking-widest">AI Categorizing...</span>
                                    </div>
                                )}
                            </div>
                        </div>

                        <div className="mt-4 pt-4 border-t border-gray-50 flex items-center justify-between">
                            <span className="text-[10px] text-gray-400 italic">Started @ {call.startTime}</span>
                            <button className="text-xs font-bold text-red-500 hover:text-red-700">Listen (Admin Only)</button>
                        </div>
                    </div>
                ))}
            </div>

            {activeCalls.length === 0 && (
                <div className="h-96 flex flex-col items-center justify-center bg-gray-50 rounded-2xl border-2 border-dashed border-gray-200">
                    <PhoneIcon className="h-12 w-12 text-gray-300 mb-4" />
                    <p className="text-gray-400 font-medium">Waiting for incoming citizen calls...</p>
                </div>
            )}
        </div>
    );
};

export default LiveMonitor;
