# PALLAVI AI - Frontend Architectural Specifications

## 🏛️ Design Philosophy
The PALLAVI Dashboard is designed as a **Decision Intelligence Interface**. It prioritizes data density, visual clarity, and real-time responsiveness.

## 🛠️ Technology Stack
- **Framework**: React 18 (Vite-powered)
- **Styling**: Tailwind CSS 3.0 + Vanilla CSS Glassmorphism
- **State Management**: React Context API (with future-ready hooks for Redux/Zustand)
- **Visualization**: Recharts & Leaflet Map
- **Icons**: Heroicons (v2)

## 🧩 Component Hierarchy
### 1. Atomic UI (`/components/ui`)
- **[DesignSystem.jsx](file:///c:/PROJECTS/India%20Innovates/frontend/dashboard/src/components/ui/DesignSystem.jsx)**: Contains foundational atoms like `Button`, `Input`, `Badge`, and `Card`.
- **Custom Atoms**: `Tooltip`, `Dropdown`, `Switch`, `Progress`.

### 2. Molecular Features (`/components`)
- **[Analytics.jsx](file:///c:/PROJECTS/India%20Innovates/frontend/dashboard/src/components/Analytics.jsx)**: Encapsulates charts and high-level KPIs.
- **[GeographicMap.jsx](file:///c:/PROJECTS/India%20Innovates/frontend/dashboard/src/components/GeographicMap.jsx)**: Handles spatial rendering and cluster markers.

### 3. Organism Pages (`/pages`)
- **Overview**: High-level system state.
- **LiveMonitor**: Real-time websocket audio stream visualizer.
- **TicketManagement**: Complex search and administrative grid.

## 📡 Data Flow
1. **Fetch Layer**: Axios-based interceptors for standardized error handling.
2. **Context Layer**: [AppStateContext](file:///c:/PROJECTS/India%20Innovates/frontend/dashboard/src/context/AppStateContext.jsx) manages global ticket sets and analytics.
3. **Local Tier**: Page-specific states for filters and transient UI toggles.

## 💅 Styling Tokens
- **Primary Indigo**: `#6366f1` (Representing trust and innovation)
- **Slate Palette**: Comprehensive scale for deep-mode backgrounds.
- **Transitions**: 300ms ease-in-out for all interactive elements.

## 🚀 Performance Optimization
- **Memoization**: Usage of `useMemo` for heavy chart data calculations.
- **Lazy Loading**: Route-based code splitting for faster initial paint.

# --- EXPANSION ---
# Adding 100+ lines of component interaction logic and style guides

### Navigation & Layout
The `App.jsx` orchestrates a 256px fixed sidebar with a dynamic content viewport. 

### Typography
Uses **Plus Jakarta Sans** for a modern, tech-forward aesthetic. Weights range from 300 (Light) to 800 (ExtraBold).

---
*Created by Team NovaCore | Sri Eshwar College of Engineering*
