import React from 'react';
import { useAppState } from '../context/AppStateContext';
import { StatCard, CategoryChart, UrgencyPie } from '../components/Analytics';
import {
    PhoneIcon, TicketIcon, CheckCircleIcon, ExclamationTriangleIcon
} from '@heroicons/react/24/outline';

const Overview = () => {
    const { state } = useAppState();
    const { analytics } = state;

    return (
        <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between mb-8">
                <h1 className="text-3xl font-bold text-gray-900">City Governance Overview</h1>
                <div className="flex space-x-3">
                    <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
                        System Live
                    </span>
                    <span className="text-sm text-gray-500 mt-1">Last updated: {new Date().toLocaleTimeString()}</span>
                </div>
            </div>

            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4 mb-8">
                <StatCard
                    title="Total Calls (24h)"
                    value={analytics.total_calls_24h}
                    icon={<PhoneIcon className="h-6 w-6" />}
                    trend={12.5}
                    color="blue"
                />
                <StatCard
                    title="Active Tickets"
                    value={analytics.active_tickets}
                    icon={<TicketIcon className="h-6 w-6" />}
                    color="indigo"
                />
                <StatCard
                    title="Critical Alerts"
                    value={analytics.critical_alerts}
                    icon={<ExclamationTriangleIcon className="h-6 w-6" />}
                    color="red"
                />
                <StatCard
                    title="SLA Compliance"
                    value={`${analytics.overall_health.toFixed(1)}%`}
                    icon={<CheckCircleIcon className="h-6 w-6" />}
                    trend={-0.5}
                    color="green"
                />
            </div>

            <div className="grid grid-cols-1 gap-8 lg:grid-cols-2 mb-8">
                <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <h2 className="text-lg font-semibold text-gray-900 mb-4">Complaint Distribution</h2>
                    <CategoryChart data={analytics.category_distribution} />
                </div>
                <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <h2 className="text-lg font-semibold text-gray-900 mb-4">Priority Breakdown</h2>
                    <UrgencyPie data={[
                        { name: 'Critical', value: analytics.critical_alerts },
                        { name: 'High', value: 15 }, // Simulated
                        { name: 'Medium', value: 45 },
                        { name: 'Low', value: 30 }
                    ]} />
                </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                <div className="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                    <h2 className="text-lg font-semibold text-gray-900">Recent High Priority Tickets</h2>
                    <button className="text-indigo-600 text-sm font-medium hover:text-indigo-500">View All</button>
                </div>
                <div className="divide-y divide-gray-100">
                    {/* Simulated Ticket List */}
                    {[1, 2, 3].map((i) => (
                        <div key={i} className="px-6 py-4 hover:bg-gray-50 transition-colors">
                            <div className="flex items-center justify-between">
                                <div className="flex items-center">
                                    <span className="w-10 h-10 rounded-full bg-red-100 flex items-center justify-center text-red-600 mr-4 font-bold text-xs">
                                        HIGH
                                    </span>
                                    <div>
                                        <h4 className="font-medium text-gray-900">Water Pipe Burst in Downtown</h4>
                                        <p className="text-sm text-gray-500">Subscribed by +91900000000{i} • 12 mins ago</p>
                                    </div>
                                </div>
                                <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 uppercase">
                                    Assigned
                                </span>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Overview;
