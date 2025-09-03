import {Anchor, Group, Progress, Table, Text, Tree, TreeNodeData,RenderTreeNodePayload} from '@mantine/core';
import { IconFolder, IconFolderOpen } from '@tabler/icons-react';
import classes from '../assets/css/Toolchain.module.css';
import {useEffect, useState} from "react";
import {useCoreContext} from "../context/CoreContext";


export function Projects() {

    const {projects, refreshProjects } = useCoreContext();

    useEffect(()=>{
        refreshProjects()
    },[])

    useEffect(() => {
        return () => {
            console.log("Update toolchain data")

            // let newData = deepConstructToolchainTree(projects)
            // console.log(newData)
            // setProjectTree( deepConstructToolchainTree(projects) )
        };
    }, [projects]);
    const rows = projects.map((row) => {
        // const totalReviews = row.reviews.negative + row.reviews.positive;
        // const positiveReviews = (row.reviews.positive / totalReviews) * 100;
        // const negativeReviews = (row.reviews.negative / totalReviews) * 100;

        return (
            <Table.Tr key={row.id}>
                <Table.Td>
                    <Anchor component="button" fz="sm">
                        {row.name}
                    </Anchor>
                </Table.Td>
                <Table.Td>{row.version} ({row.auto_version})</Table.Td>
                <Table.Td>
                    <Anchor component="button" fz="sm">
                        {row.path}
                    </Anchor>
                </Table.Td>
                <Table.Td>{row.options}</Table.Td>
                <Table.Td>{row.libs}</Table.Td>
                <Table.Td>{row.configs}</Table.Td>
                <Table.Td>
                    <Group justify="space-between">
                        <Text fz="xs" c="teal" fw={700}>
                            {0}%
                        </Text>
                        <Text fz="xs" c="red" fw={700}>
                            {0}%
                        </Text>
                    </Group>
                    <Progress.Root>
                        <Progress.Section
                            className={classes.progressSection}
                            value={0}
                            color="teal"
                        />

                        <Progress.Section
                            className={classes.progressSection}
                            value={0}
                            color="red"
                        />
                    </Progress.Root>
                </Table.Td>
            </Table.Tr>
        );
    });

    return (
        <Table.ScrollContainer minWidth={800}>
            <Table verticalSpacing="xs">
                <Table.Thead>
                    <Table.Tr>
                        <Table.Th>Project</Table.Th>
                        <Table.Th>Ver</Table.Th>
                        <Table.Th>Path</Table.Th>
                        <Table.Th>Libs</Table.Th>
                        <Table.Th>Options</Table.Th>
                        <Table.Th>Configs</Table.Th>
                        <Table.Th>Progress</Table.Th>
                        <Table.Th>Actions</Table.Th>
                    </Table.Tr>
                </Table.Thead>
                <Table.Tbody>{rows}</Table.Tbody>
            </Table>
        </Table.ScrollContainer>
    );
}
