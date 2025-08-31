import React, {createContext, useContext, useState} from 'react';
import {useApi} from "./ApiContext";

export enum CCToolPage {
    dashboard= 'dashboard',
    projects = "projects",
    toolchains = "toolchains"
}

export enum SystemEnum {
    linux = "Linux",
    macOS = "MacOS",
    windows = "Windows",
    iOS = "iOS",
    android = "Android",
    jniLinux = "JNI_Linux",
    jniAndroid = "JNI_Android"
}

export interface Hardware {
    brand:string,
    chip:string,
    arch:string,
    abi:string,
    libc:string
}

export interface Project {
    name:string,
    path:string,
    version:string,
    auto_version:number
}

export interface Platform {
    system: SystemEnum,
    hardware: Hardware
}

export enum ArchiveExt {
    tar = ".tar",
    tg = ".tar.gz",
    tz = ".tar.xz",
    xz = ".xz",
    zip = ".zip"
}

export interface Archive {
    url:string,
    filename:string,
    path:string,
    md5:string|null,
    sha1:string|null,
    sha256:string|null,
    ext: ArchiveExt
}

export interface Binaries {
    cc:string,
    cpp:string,
    gpp:string, // g++
    as: string,
    ar: string,
    ranlib: string,
    ld: string,
    objcopy: string,
    objdump: string,
    strip: string,
    strings: string,
    nm: string,
    windres: string | null
}

export interface Toolchain {
    name:string,
    version:string,
    platform: Platform,
    archive: Archive,
    binaries: Binaries
}

export interface ToolchainInfo {
    arch: {
        standard:{
            version:{
                tree_info:{

                }
                host_os:{
                    host_arch:{

                    }
                }
            }
        }
    }
}

type CoreContextType =
{
    currentPage: CCToolPage
    setCurrentPage: (page:CCToolPage)=>void

    projects: Project[]

    toolchains: Toolchain[]
    refreshToolchains: ()=>void
}

const CoreContext = createContext<CoreContextType>({
    currentPage: CCToolPage.dashboard,
    setCurrentPage: ()=>{},
    projects:[],
    toolchains:[],
    refreshToolchains:()=>{}
});


export const CoreProvider = ({children} : {children: React.ReactNode}) => {

    const [currentPage, setCurrentPage] = useState(CCToolPage.dashboard);
    const [projects, setProjects] = useState<Project[]>([]);
    const [toolchains, setToolchains] = useState<Toolchain[]>([])

    const { data, loading, error, fetchData } = useApi();

    const refreshToolchainsWithApi = ()=>{
        fetchData('/api/getToolchains').then(dt=>{
            if (dt)
            {
                console.log("Toolchain get ok", dt)
                setToolchains(dt)
            }
        })
    }

    const contextValue: CoreContextType = {
        currentPage:currentPage,
        setCurrentPage:setCurrentPage,
        projects: projects,
        toolchains: toolchains,
        refreshToolchains: refreshToolchainsWithApi
    }

    return (
        <CoreContext.Provider value={contextValue}>
            {children}
        </CoreContext.Provider>
    )
}


export const useCoreContext = ()=> useContext(CoreContext)