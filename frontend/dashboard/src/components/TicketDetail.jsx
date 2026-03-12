import React from 'react';

const TicketDetail = ({ ticket, onClose }) => {
    if (!ticket) return null;

    return (
        <div className="fixed inset-0 z-50 overflow-y-auto bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4">
            <div className="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-hidden flex flex-col">
                <div className="p-6 border-b border-slate-100 flex items-center justify-between">
                    <div>
                        <span className="text-xs font-black text-indigo-500 uppercase tracking-widest">Case Details</span>
                        <h2 className="text-2xl font-black text-slate-900 leading-tight mt-1">{ticket.ticket_id}</h2>
                    </div>
                    <button onClick={onClose} className="p-2 hover:bg-slate-50 rounded-full transition-colors">
                        <svg className="w-6 h-6 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <div className="p-8 overflow-y-auto space-y-8">
                    <div>
                        <h4 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-3">Citizens Statement</h4>
                        <div className="bg-slate-50 p-6 rounded-xl border border-slate-100">
                            <p className="text-slate-800 leading-relaxed italic font-serif text-lg">"{ticket.complaint_text}"</p>
                        </div>
                    </div>

                    <div className="grid grid-cols-2 gap-8 text-sm">
                        <div>
                            <p className="text-slate-400 font-bold uppercase tracking-tight mb-2">Category</p>
                            <div className="flex items-center space-x-2">
                                <div className="w-2 h-2 bg-indigo-500 rounded-full"></div>
                                <span className="font-black text-slate-900">{ticket.category}</span>
                            </div>
                        </div>
                        <div>
                            <p className="text-slate-400 font-bold uppercase tracking-tight mb-2">Current Priority</p>
                            <span className={`font-black uppercase tracking-tighter ${ticket.priority === 'CRITICAL' ? 'text-red-600 animate-pulse' : 'text-slate-900'}`}>
                                {ticket.priority}
                            </span>
                        </div>
                        <div>
                            <p className="text-slate-400 font-bold uppercase tracking-tight mb-2">Current Status</p>
                            <span className="px-3 py-1 bg-green-50 text-green-700 font-black rounded-lg text-xs uppercase">
                                {ticket.status}
                            </span>
                        </div>
                        <div>
                            <p className="text-slate-400 font-bold uppercase tracking-tight mb-2">SLA Time Remaining</p>
                            <span className="font-mono text-slate-900 font-bold">03h : 42m : 11s</span>
                        </div>
                    </div>

                    <div>
                        <h4 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">Audit Trail</h4>
                        <div className="space-y-4">
                            {[1, 2].map(i => (
                                <div key={i} className="flex items-start space-x-4">
                                    <div className="w-1 h-full bg-slate-100 absolute left-[2.25rem]"></div>
                                    <div className="w-3 h-3 rounded-full bg-indigo-500 mt-1 relative z-10 border-4 border-white"></div>
                                    <div>
                                        <p className="text-xs font-bold text-slate-900">Status changed from Received to Assigned</p>
                                        <p className="text-[10px] text-slate-400 mt-0.5">Automated AI Routing • 12:44 PM • 12 Mar 2026</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

                <div className="p-6 bg-slate-50 border-t border-slate-100 flex justify-end space-x-4">
                    <button className="px-6 py-2.5 text-sm font-bold text-red-600 hover:bg-red-50 rounded-xl transition-all uppercase tracking-widest">Escalate Now</button>
                    <button className="px-8 py-2.5 bg-indigo-600 text-white rounded-xl shadow-xl shadow-indigo-500/20 font-black text-sm uppercase tracking-widest hover:bg-indigo-700 transition-all">Mark as Resolved</button>
                </div>
            </div>
        </div>
    );
};

export default TicketDetail;
