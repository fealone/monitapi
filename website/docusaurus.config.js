module.exports = {
  title: 'monitapi',
  tagline: 'monitapi is something to monitor API(URL) by a serverless.',
  url: 'https://fealone.github.io/monitapi',
  baseUrl: '/monitapi/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.png',
  organizationName: 'fealone', // Usually your GitHub org/user name.
  projectName: 'monitapi', // Usually your repo name.
  themeConfig: {
    image: 'img/ogimg.png',
    navbar: {
      title: 'monitapi',
      logo: {
        alt: 'monitapi Logo',
        src: 'img/favicon.png',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/fealone/monitapi',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Intoroduction',
              to: 'docs/',
            },
            {
              label: 'Documents',
              to: 'docs/definition',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Twitter',
              href: 'https://twitter.com/xfealonex',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              href: 'https://lonesec.com/',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/fealone/monitapi',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} fealone.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/fealone/monitapi/edit/master/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
