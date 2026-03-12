import React from 'react';

export const Button = ({ children, variant = 'primary', size = 'md', className = '', ...props }) => {
    const variants = {
        primary: 'bg-indigo-600 text-white hover:bg-indigo-700 shadow-indigo-500/20',
        secondary: 'bg-slate-800 text-slate-100 hover:bg-slate-700',
        outline: 'border-2 border-slate-200 text-slate-600 hover:border-indigo-600 hover:text-indigo-600',
        ghost: 'text-slate-500 hover:bg-slate-100',
        danger: 'bg-rose-500 text-white hover:bg-rose-600'
    };

    const sizes = {
        sm: 'px-3 py-1.5 text-xs',
        md: 'px-5 py-2.5 text-sm',
        lg: 'px-8 py-3.5 text-base'
    };

    return (
        <button
            className={`inline-flex items-center justify-center font-bold rounded-xl transition-all duration-300 active:scale-95 disabled:opacity-50 ${variants[variant]} ${sizes[size]} ${className}`}
            {...props}
        >
            {children}
        </button>
    );
};

export const Input = ({ label, error, className = '', ...props }) => (
    <div className="flex flex-col gap-1.5 w-full">
        {label && <label className="text-xs font-black text-slate-400 uppercase tracking-widest">{label}</label>}
        <input
            className={`w-full bg-white border border-slate-200 rounded-xl px-4 py-3 text-sm focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all outline-none ${error ? 'border-rose-500 bg-rose-50' : ''} ${className}`}
            {...props}
        />
        {error && <p className="text-[10px] font-bold text-rose-500 mt-1">{error}</p>}
    </div>
);

export const Badge = ({ status, children }) => {
    const styles = {
        open: 'bg-sky-100 text-sky-700 border-sky-200',
        resolved: 'bg-emerald-100 text-emerald-700 border-emerald-200',
        pending: 'bg-amber-100 text-amber-700 border-amber-200',
        critical: 'bg-rose-100 text-rose-700 border-rose-200'
    };

    return (
        <span className={`px-2.5 py-1 rounded-full text-[10px] font-black uppercase tracking-widest border ${styles[status]}`}>
            {children || status}
        </span>
    );
};

export const Card = ({ title, subtitle, icon: Icon, children, className = '' }) => (
    <div className={`bg-white rounded-3xl border border-slate-100 p-6 shadow-sm hover:shadow-md transition-all ${className}`}>
        <div className="flex items-start justify-between mb-4">
            <div>
                {title && <h3 className="font-extrabold text-slate-800">{title}</h3>}
                {subtitle && <p className="text-xs text-slate-400 font-medium">{subtitle}</p>}
            </div>
            {Icon && (
                <div className="p-3 bg-indigo-50 rounded-2xl text-indigo-600">
                    <Icon className="w-5 h-5" />
                </div>
            )}
        </div>
        {children}
    </div>
);
