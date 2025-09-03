import {Anchor, Group, Progress, Table, Text, Tree, TreeNodeData,RenderTreeNodePayload} from '@mantine/core';
import { IconFolder, IconFolderOpen } from '@tabler/icons-react';
import classes from '../assets/css/Toolchain.module.css';
import {useEffect, useState} from "react";
import {useCoreContext} from "../context/CoreContext";

interface FileIconProps {
    name: string;
    isFolder: boolean;
    expanded: boolean;
}


function FileIcon({ name, isFolder, expanded }: FileIconProps) {
    if (name.endsWith('package.json')) {
        return <NpmIcon size={14} />;
    }

    if (name.endsWith('.ts') || name.endsWith('.tsx') || name.endsWith('tsconfig.json')) {
        return <TypeScriptCircleIcon size={14} />;
    }

    if (name.endsWith('.css')) {
        return <CssIcon size={14} />;
    }

    if (isFolder) {
        return expanded ? (
            <IconFolderOpen color="var(--mantine-color-yellow-9)" size={14} stroke={2.5} />
        ) : (
            <IconFolder color="var(--mantine-color-yellow-9)" size={14} stroke={2.5} />
        );
    }

    return null;
}


function Leaf({ node, expanded, hasChildren, elementProps }: RenderTreeNodePayload) {
    return (
        <Group gap={5} {...elementProps}>
            <FileIcon name={node.value} isFolder={hasChildren} expanded={expanded} />
            <span>{node.label}</span>
        </Group>
    );
}

function deepConstructToolchainTree( toolchainData ): TreeNodeData[]
{
    let dataTree:TreeNodeData[] = []

    for (let k in toolchainData)
    {
        if( typeof toolchainData[k] == "string")
        {
            let data = {
                value: k,
                label: toolchainData[k]
            }
            dataTree.push(data)
        }
        else if ( typeof toolchainData[k] != 'object' )
        {
            let data = {
                value: k,
                label: k
            }
            dataTree.push(data)
        }
        else{
            let data = {
                value:k,
                label: k,
                children: deepConstructToolchainTree(toolchainData[k])
            }
            dataTree.push(data)
        }
    }
    return dataTree
}

export function Toolchain() {

    const {toolchains, refreshToolchains } = useCoreContext();

    const [toolchainTree, setToolchainTree] = useState<TreeNodeData[]>([{"value":"none","label":"No toolchain found"}]);

    useEffect(()=>{
        refreshToolchains()
    },[])

    useEffect(() => {
        return () => {
            console.log("Update toolchain data")

            let newData = deepConstructToolchainTree(toolchains)
            console.log(newData)
            setToolchainTree( deepConstructToolchainTree(toolchains) )
        };
    }, [toolchains]);

    return (
        <Tree
            data={toolchainTree}
            renderNode={(payload) => <Leaf {...payload} />}
        />
    );
}