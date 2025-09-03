import {useDisclosure} from '@mantine/hooks';
import {AppShell, Burger, Code, Group, Text} from "@mantine/core";
import {Navbar} from "./NavBar";
import {IconCircleDottedLetterC} from "@tabler/icons-react";
import {CCToolPage, useCoreContext} from "./context/CoreContext";
import {Toolchain} from "./Pages/Toolchains";
import {Projects} from "./Pages/Projects"

export function Layout() {
    const [opened, { toggle }] = useDisclosure();

    const { currentPage} = useCoreContext();

    // @ts-ignore
    return (
        <AppShell
            header={{ height: 60 }}
            footer={{ height: 60 }}
            navbar={{ width: 340, breakpoint: 'sm', collapsed: { mobile: !opened } }}
            aside={{ width: 360, breakpoint: 'md', collapsed: { desktop: false, mobile: true } }}
            padding="md"
        >
            <AppShell.Header>
                <Group h="100%" px="md">
                    <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
                    <IconCircleDottedLetterC size={32} color={'blue'}/>
                    <Text>CCROOT Web Tool</Text>
                    <Code fw={700}>v0.1.2</Code>
                </Group>
            </AppShell.Header>
            <AppShell.Navbar p="md">
                <Navbar/>
            </AppShell.Navbar>

            <AppShell.Main pl={0} pt={50}>
                {
                    currentPage == CCToolPage.dashboard &&
                    <Text>Dashboard</Text>
                }
                {
                    currentPage == CCToolPage.projects &&
                    <Projects/>
                }
                {
                    currentPage == CCToolPage.toolchains &&
                    <Toolchain/>
                }
            </AppShell.Main>

            <AppShell.Aside p="md">

            </AppShell.Aside>

            <AppShell.Footer p="md">

            </AppShell.Footer>
        </AppShell>
    );
}