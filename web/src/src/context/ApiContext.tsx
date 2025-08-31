import { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

// 定义 Context 类型（TypeScript）
interface ApiContextType {
    data: any;
    loading: boolean;
    error: string | null;
    apiBaseUrl: string; // 动态后端地址
    fetchData: (endpoint: string) => Promise<any>;
    postData: (endpoint: string, payload: any) => Promise<any>;
}

// 创建 Context
const ApiContext = createContext<ApiContextType | null>(null);

// Provider 组件
export function ApiProvider({ children }: { children: React.ReactNode }) {
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // 动态配置后端地址（默认开发环境）
    const apiBaseUrl = 'http://127.0.0.1:1688';

    // 封装 GET 请求
    const fetchData = async (endpoint: string) => {
        try {
            setLoading(true);
            const response = await axios.get(`${apiBaseUrl}${endpoint}`);
            setError(null);
            return response.data;
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unknown error');
        } finally {
            setLoading(false);
        }
    };

    // 封装 POST 请求
    const postData = async (endpoint: string, payload: any) => {
        try {
            setLoading(true);
            const response = await axios.post(`${apiBaseUrl}${endpoint}`, payload);
            setError(null);
            return response.data
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unknown error');
        } finally {
            setLoading(false);
        }
    };

    // 暴露的 Context 值
    const value = {
        data,
        loading,
        error,
        apiBaseUrl, // 允许组件访问当前后端地址
        fetchData,
        postData,
    };

    return <ApiContext.Provider value={value}>{children}</ApiContext.Provider>;
}

// 自定义 Hook
export function useApi() {
    const context = useContext(ApiContext);
    if (!context) {
        throw new Error('useApi must be used within an ApiProvider');
    }
    return context;
}