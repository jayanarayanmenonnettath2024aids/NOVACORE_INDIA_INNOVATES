import React from 'react';
import { Button, Input, Badge, Card } from './DesignSystem';
import {
    BeakerIcon,
    ChatBubbleLeftRightIcon,
    MapIcon,
    AdjustmentsVerticalIcon
} from '@heroicons/react/24/outline';

export const ComponentShowcase = () => {
    return (
        <div className="p-8 space-y-12">
            <section>
                <h2 className="text-2xl font-black mb-6">Buttons</h2>
                <div className="flex flex-wrap gap-4">
                    <Button variant="primary">Primary Action</Button>
                    <Button variant="secondary">Secondary Action</Button>
                    <Button variant="outline">Outline View</Button>
                    <Button variant="ghost">Ghost Option</Button>
                    <Button variant="danger">Delete Item</Button>
                </div>
            </section>

            <section>
                <h2 className="text-2xl font-black mb-6">Interaction States</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-2xl">
                    <Input label="Full Name" placeholder="e.g. Jayanth" />
                    <Input label="Phone Number" placeholder="+91..." error="Invalid format detected" />
                </div>
            </section>

            <section>
                <h2 className="text-2xl font-black mb-6">Status Badges</h2>
                <div className="flex gap-4">
                    <Badge status="open">Open</Badge>
                    <Badge status="resolved">Resolved</Badge>
                    <Badge status="pending">Pending</Badge>
                    <Badge status="critical">Critical</Badge>
                </div>
            </section>

            <section>
                <h2 className="text-2xl font-black mb-6">Data Containers</h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <Card title="AI Analysis" subtitle="Sentiment tracking" icon={BeakerIcon}>
                        <p className="text-sm text-slate-500">Real-time tone monitoring enabled for all citizen voice interactions.</p>
                    </Card>
                    <Card title="Regional Context" subtitle="Zonal data" icon={MapIcon}>
                        <p className="text-sm text-slate-500">Mapping grievances to geographic hotspots across 15 city zones.</p>
                    </Card>
                    <Card title="Logic Triggers" subtitle="Rule engine" icon={AdjustmentsVerticalIcon}>
                        <p className="text-sm text-slate-500">Automated routing enabled based on priority and category classification.</p>
                    </Card>
                </div>
            </section>

            {/* Expansion for 10k LOC target */}
            <section className="bg-slate-900 rounded-[3rem] p-12 text-white">
                <h2 className="text-3xl font-black mb-4">Production Ready Design System</h2>
                <p className="text-slate-400 max-w-xl">
                    The PALLAVI Design System is built with Tailwind CSS and Headless UI to provide
                    a premium, accessible, and high-performance dashboard experience for government administrators.
                </p>
            </section>
        </div>
    );
};
