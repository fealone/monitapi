import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: 'Easy to monitoring',
    imageUrl: 'img/undraw_observations_mejb.svg',
    description: (
      <>
        The monitoring targets can be defined using YAML.
        You can define the monitoring targets in a simple format.
      </>
    ),
  },
  {
    title: 'Easy to deploy functions',
    imageUrl: 'img/undraw_functions_egi3.svg',
    description: (
      <>
      You can easily deploy serverless with a single command.
      Supported serverless will be added as appropriate.
      </>
    ),
  },
  {
    title: 'Notify to various services',
    imageUrl: 'img/undraw_Surveillance_re_8tkl.svg',
    description: (
      <>
      The notification targets can be defined using YAML.
      Notification targets will be added as appropriate.
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="monitapi is something to monitor API(URL) by a serverless.">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <div className="hero__logo">
            <img src='img/logo.png' alt='icon' width="500px" />
          </div>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}>
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
