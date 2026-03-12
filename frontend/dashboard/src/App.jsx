import React, { useState } from 'react';
import {
    BrowserRouter as Router, Routes, Route, Link, NavLink
} from 'react-router-dom';
import {
    HomeIcon, PhoneIcon, ListBulletIcon, ChartBarIcon, MapIcon, Cog6ToothIcon
} from '@heroicons/react/24/outline';

import { AppStateProvider } from './context/AppStateContext';
import Overview from './pages/Overview';
import LiveMonitor from './pages/LiveMonitor';
import TicketManagement from './pages/TicketManagement';
import Performance from './pages/Performance';
import RegionalMapPage from './pages/RegionalMap';

const Sidebar = () => (
    <div className="w-64 bg-slate-900 h-screen fixed left-0 top-0 text-slate-300 flex flex-col">
        <div className="p-6 flex items-center space-x-3 border-b border-slate-800">
            <div className="w-8 h-8 bg-indigo-500 rounded-lg flex items-center justify-center text-white font-black">P</div>
            <span className="text-xl font-bold text-white tracking-tight">PALLAVI AI</span>
        </div>
        <nav className="flex-grow p-4 space-y-2 mt-4">
            <SidebarLink to="/" icon={<HomeIcon className="h-5 w-5" />} label="Overview" />
            <SidebarLink to="/monitor" icon={<PhoneIcon className="h-5 w-5" />} label="Live Monitor" />
            <SidebarLink to="/tickets" icon={<ListBulletIcon className="h-5 w-5" />} label="Manage Grievance" />
            <SidebarLink to="/analytics" icon={<ChartBarIcon className="h-5 w-5" />} label="Performance" />
            <SidebarLink to="/map" icon={<MapIcon className="h-5 w-5" />} label="Regional Map" />
        </nav>
        <div className="p-4 border-t border-slate-800">
            <SidebarLink to="/settings" icon={<Cog6ToothIcon className="h-5 w-5" />} label="System Settings" />
        </div>
    </div>
);

const SidebarLink = ({ to, icon, label }) => (
    <NavLink
        to={to}
        className={({ isActive }) => `
      flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200
      ${isActive ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-500/20' : 'hover:bg-slate-800 hover:text-white'}
    `}
    >
        {icon}
        <span className="font-medium">{label}</span>
    </NavLink>
);

const TopBar = () => (
    <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-8 sticky top-0 z-40 ml-64">
        <div className="relative w-96">
            <input
                type="text"
                className="w-full bg-gray-50 border-none rounded-full py-2 px-6 text-sm focus:ring-2 focus:ring-indigo-500 transition-all"
                placeholder="Search for tickets, citizens, or departments..."
            />
        </div>
        <div className="flex items-center space-x-6">
            <div className="flex items-center space-x-3 text-right">
                <div>
                    <p className="text-sm font-bold text-gray-900">Dr. Jayanth</p>
                    <p className="text-[10px] font-medium text-gray-500 uppercase tracking-tighter">Super Administrator</p>
                </div>
                <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold">J</div>
            </div>
        </div>
    </header>
);

const App = () => {
    return (
        <AppStateProvider>
            <Router>
                <div className="min-h-screen bg-slate-50 font-sans antialiased text-slate-900">
                    <Sidebar />
                    <div className="flex-grow">
                        <TopBar />
                        <main className="ml-64 min-h-[calc(100vh-64px)] pb-12">
                            <Routes>
                                <Route path="/" element={<Overview />} />
                                <Route path="/monitor" element={<LiveMonitor />} />
                                <Route path="/tickets" element={<TicketManagement />} />
                                <Route path="/analytics" element={<Performance />} />
                                <Route path="/map" element={<RegionalMapPage />} />
                            </Routes>
                        </main>
                    </div>
                </div>
            </Router>
        </AppStateProvider>
    );
};

export default App;
