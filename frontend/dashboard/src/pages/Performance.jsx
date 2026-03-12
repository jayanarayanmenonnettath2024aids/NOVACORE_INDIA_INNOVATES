import React from 'react';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
    AreaChart, Area, ComposedChart, Bar
} from 'recharts';
import { useAppState } from '../context/AppStateContext';

const Performance = () => {
    const { state } = useAppState();

    // Simulated trend data for high-fidelity visualization
    const trendData = [
        { name: 'Mon', calls: 400, resolved: 240, avgTime: 12 },
        { name: 'Tue', calls: 300, resolved: 139, avgTime: 15 },
        { name: 'Wed', calls: 200, resolved: 980, avgTime: 8 },
        { name: 'Thu', calls: 278, resolved: 390, avgTime: 10 },
        { name: 'Fri', calls: 189, resolved: 480, avgTime: 11 },
        { name: 'Sat', calls: 239, resolved: 380, avgTime: 14 },
        { name: 'Sun', calls: 349, resolved: 430, avgTime: 9 },
    ];

    return (
        <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
                <h1 className="text-3xl font-black text-slate-900 tracking-tight">Performance Analytics</h1>
                <p className="text-slate-500 mt-2">Deep-dive into department efficiency and call volume trends.</p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
                <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
                    <div className="flex items-center justify-between mb-6">
                        <h3 className="text-lg font-bold text-slate-900">Call Resolution Trends</h3>
                        <select className="text-sm border-none bg-slate-50 rounded-lg focus:ring-2 focus:ring-indigo-500">
                            <option>Last 7 Days</option>
                            <option>Last 30 Days</option>
                        </select>
                    </div>
                    <div className="h-80">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={trendData}>
                                <defs>
                                    <linearGradient id="colorCalls" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#6366f1" stopOpacity={0.1} />
                                        <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
                                    </linearGradient>
                                </defs>
                                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: '#94a3b8', fontSize: 12 }} />
                                <YAxis axisLine={false} tickLine={false} tick={{ fill: '#94a3b8', fontSize: 12 }} />
                                <Tooltip
                                    contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }}
                                />
                                <Area type="monotone" dataKey="calls" stroke="#6366f1" fillOpacity={1} fill="url(#colorCalls)" strokeWidth={3} />
                                <Area type="monotone" dataKey="resolved" stroke="#10b981" fillOpacity={0} strokeWidth={3} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                </div>

                <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
                    <h3 className="text-lg font-bold text-slate-900 mb-6">Department vs SLA Performance</h3>
                    <div className="h-80">
                        <ResponsiveContainer width="100%" height="100%">
                            <ComposedChart data={[
                                { dept: 'Water', sla: 92, count: 45 },
                                { dept: 'Power', sla: 85, count: 68 },
                                { dept: 'Roads', sla: 78, count: 120 },
                                { dept: 'Clean', sla: 95, count: 32 },
                                { dept: 'Safety', sla: 88, count: 15 },
                            ]}>
                                <CartesianGrid stroke="#f1f5f9" vertical={false} />
                                <XAxis dataKey="dept" axisLine={false} tickLine={false} />
                                <YAxis axisLine={false} tickLine={false} />
                                <Tooltip />
                                <Bar dataKey="count" fill="#e2e8f0" radius={[4, 4, 0, 0]} />
                                <Line type="monotone" dataKey="sla" stroke="#f59e0b" strokeWidth={3} dot={{ r: 6, fill: '#f59e0b', strokeWidth: 2, stroke: '#fff' }} />
                            </ComposedChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            </div>

            <div className="bg-slate-900 rounded-2xl p-8 text-white">
                <div className="flex items-center justify-between mb-8">
                    <div>
                        <h3 className="text-xl font-bold">Optimization Summary</h3>
                        <p className="text-slate-400 text-sm mt-1">AI-suggested improvements for city administrative response.</p>
                    </div>
                    <button className="px-4 py-2 bg-indigo-500 hover:bg-indigo-400 rounded-lg text-sm font-bold transition-all">Download Full Audit</button>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div className="p-6 bg-slate-800 rounded-xl border border-slate-700">
                        <span className="text-indigo-400 font-bold text-xs uppercase tracking-widest">Efficiency Boost</span>
                        <p className="mt-4 text-slate-300 leading-relaxed">Response time in <span className="text-white font-bold">Roads Dept</span> has improved by 14% since PALLAVI AI automated the triage.</p>
                    </div>
                    <div className="p-6 bg-slate-800 rounded-xl border border-slate-700">
                        <span className="text-yellow-400 font-bold text-xs uppercase tracking-widest">Attention Needed</span>
                        <p className="mt-4 text-slate-300 leading-relaxed"><span className="text-white font-bold">Power Grid</span> complaints are surging in North Zone. High probability of transformer fault.</p>
                    </div>
                    <div className="p-6 bg-slate-800 rounded-xl border border-slate-700">
                        <span className="text-green-400 font-bold text-xs uppercase tracking-widest">SLA Milestone</span>
                        <p className="mt-4 text-slate-300 leading-relaxed">Overall citizen satisfaction is at <span className="text-white font-bold">4.8/5.0</span> for the current operational cycle.</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Performance;
