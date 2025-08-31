import {useState} from 'react';
import {IconDashboard, IconFolders, IconInfoSquareRounded, IconMessage2Bolt, IconTools,} from '@tabler/icons-react';

import classes from './assets/css/Navbar.module.css';
import {CCToolPage, useCoreContext} from "./context/CoreContext";

const data = [
    { link: '', label: 'Dashboard', icon: IconDashboard, pageId: CCToolPage.dashboard },
    { link: '', label: 'Projects', icon: IconFolders, pageId: CCToolPage.projects },
    { link: '', label: 'Toolchains', icon: IconTools, pageId: CCToolPage.toolchains }
];

export function Navbar() {
    const [active, setActive] = useState('Billing');

    const {setCurrentPage} = useCoreContext()

    const links = data.map((item) => (
        <a
            className={classes.link}
            data-active={item.label === active || undefined}
            href={item.link}
            key={item.label}
            onClick={(event) => {
                event.preventDefault();
                setCurrentPage(item.pageId)
                setActive(item.label);
            }}
        >
            <item.icon className={classes.linkIcon} stroke={1.5} />
            <span>{item.label}</span>
        </a>
    ));

    return (
        <nav className={classes.navbar}>
            <div className={classes.navbarMain}>
                {links}
            </div>

            <div className={classes.footer}>
                <a href="#" className={classes.link} onClick={(event) => event.preventDefault()}>
                    <IconInfoSquareRounded className={classes.linkIcon} stroke={1.5} />
                    <span>About</span>
                </a>

                <a href="https://github.com/shezw/ccroot" className={classes.link} onClick={(event) => event.preventDefault()}>
                    <IconMessage2Bolt className={classes.linkIcon} stroke={1.5} />
                    <span>Feedback</span>
                </a>
            </div>
        </nav>
    );
}