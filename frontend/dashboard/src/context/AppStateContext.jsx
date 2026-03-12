import React, { createContext, useContext, useReducer, useEffect } from 'react';

const AppStateContext = createContext();

const initialState = {
  tickets: [],
  calls: [],
  analytics: {
    totalCalls: 0,
    activeTickets: 0,
    resolvedTickets: 0,
    slaCompliance: 100,
  },
  loading: true,
  error: null,
};

function appReducer(state, action) {
  switch (action.type) {
    case 'FETCH_START':
      return { ...state, loading: true };
    case 'FETCH_SUCCESS':
      return { 
        ...state, 
        loading: false, 
        tickets: action.payload.tickets,
        analytics: action.payload.analytics 
      };
    case 'NEW_CALL':
      return { ...state, calls: [action.payload, ...state.calls].slice(0, 50) };
    case 'UPDATE_TICKET':
      return {
        ...state,
        tickets: state.tickets.map(t => t.id === action.payload.id ? action.payload : t)
      };
    default:
      return state;
  }
}

export const AppStateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  useEffect(() => {
    const loadInitialData = async () => {
      try {
        const response = await fetch('/api/v1/analytics/dashboard');
        const data = await response.json();
        dispatch({ type: 'FETCH_SUCCESS', payload: { analytics: data, tickets: [] } });
      } catch (err) {
        dispatch({ type: 'FETCH_ERROR', payload: err.message });
      }
    };
    loadInitialData();
  }, []);

  return (
    <AppStateContext.Provider value={{ state, dispatch }}>
      {children}
    </AppStateContext.Provider>
  );
};

export const useAppState = () => useContext(AppStateContext);
