import React, { useState } from 'react';
import { useAppState } from '../context/AppStateContext';

const TicketManagement = () => {
    const [filter, setFilter] = useState('All');
    const { state } = useAppState();

    // Simulated ticket data
    const tickets = [
        { id: 'TKT-0402', citizen: 'John Doe', category: 'Water', status: 'In Progress', priority: 'High', date: '2026-03-12' },
        { id: 'TKT-0403', citizen: 'Amita Singh', category: 'Electricity', status: 'Assigned', priority: 'Medium', date: '2026-03-12' },
        { id: 'TKT-0404', citizen: 'Rahul Kumar', category: 'Sanitation', status: 'Resolved', priority: 'Low', date: '2026-03-11' },
        // Expand for scale...
    ];

    return (
        <div className="max-w-7xl mx-auto py-8 px-4">
            <div className="sm:flex sm:items-center sm:justify-between mb-8">
                <div>
                    <h1 className="text-3xl font-bold text-gray-900">Grievance Management</h1>
                    <p className="text-gray-500 mt-1">Manage, assign, and resolve citizen complaints</p>
                </div>
                <div className="mt-4 sm:mt-0 flex space-x-3">
                    <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none ring-2 ring-offset-2 ring-indigo-500">
                        Export CSV
                    </button>
                    <button className="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none ring-2 ring-offset-2 ring-indigo-500">
                        Internal Note
                    </button>
                </div>
            </div>

            <div className="bg-white shadow-sm overflow-hidden border border-gray-200 rounded-2xl">
                <div className="px-4 py-5 border-b border-gray-200 sm:px-6 bg-gray-50 flex items-center justify-between">
                    <div className="flex space-x-4">
                        {['All', 'Active', 'Resolved', 'SLA Breached'].map(tab => (
                            <button
                                key={tab}
                                onClick={() => setFilter(tab)}
                                className={`px-3 py-1 rounded-full text-sm font-medium ${filter === tab ? 'bg-indigo-100 text-indigo-700' : 'text-gray-500 hover:text-gray-700'}`}
                            >
                                {tab}
                            </button>
                        ))}
                    </div>
                    <div className="relative rounded-md shadow-sm">
                        <input
                            type="text"
                            className="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
                            placeholder="Search tickets..."
                        />
                    </div>
                </div>
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-white">
                        <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ticket ID</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Citizen</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Priority</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {tickets.map((ticket) => (
                            <tr key={ticket.id} className="hover:bg-gray-50 transition-colors">
                                <td className="px-6 py-4 whitespace-nowrap text-sm font-bold text-indigo-600">{ticket.id}</td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">{ticket.citizen}</td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{ticket.category}</td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase ${ticket.priority === 'High' ? 'bg-red-100 text-red-700' :
                                            ticket.priority === 'Medium' ? 'bg-yellow-100 text-yellow-700' : 'bg-blue-100 text-blue-700'
                                        }`}>
                                        {ticket.priority}
                                    </span>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <span className="flex items-center text-sm text-gray-500">
                                        <span className="h-2 w-2 rounded-full bg-green-500 mr-2"></span>
                                        {ticket.status}
                                    </span>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                    <button className="text-indigo-600 hover:text-indigo-900 mr-3">View</button>
                                    <button className="text-gray-400 hover:text-gray-600">Edit</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default TicketManagement;
