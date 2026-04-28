**STUDIOYOU — CONFIDENTIAL RESEARCH**

**Building a Creator Asset Vault**

Technical Reality and Business Viability

March 2026  |  Pre-Seed Research  |  Confidential

| Bottom line: A universal creator data portability engine is technically buildable but operationally grueling — and the standalone business case is thin. The strongest play is as a core infrastructure module within StudioYou, with a B2B compliance wedge targeting EU DMA-regulated platforms. |
| :---- |

# **The Technical Stack**

## **What Exists and What's Buildable**

The conversion and metadata layer is largely a solved problem. The following open-source components cover 60-70% of the required infrastructure with no custom build needed:

| Tool / Standard | What It Does | License |
| :---- | :---- | :---- |
| FFmpeg | Handles virtually every video/audio format conversion | LGPL / GPL |
| ImageMagick | Covers 200+ image formats | Apache 2.0 |
| ExifTool | Metadata read/write including IPTC 2025.1 AI fields | Open Source |
| C2PA SDK (Rust / Python / JS) | Cryptographically signed provenance manifests | Apache 2.0 |
| IPTC 2025.1 | Standardized AI metadata fields (prompt, model, version) | Open Standard |
| DTI Data Transfer Project | Platform adapter architecture and canonical data models | Apache 2.0 |

The C2PA specification is now at v2.2 with 6,000+ member organizations and production-ready SDKs from Adobe, Microsoft, OpenAI, and Google. The IPTC Photo Metadata Standard 2025.1 (November 2025\) added four AI-specific fields — AI System Used, AI System Version, AI Prompt Information, and AI Prompt Writer Name — with ExifTool support since v13.40. These are the building blocks of a standardized creator asset container.

## **Platform-by-Platform API Reality**

The real difficulty is not file conversion — it is the platform API trench warfare required to extract meaningful creator data. Each platform has fundamentally different access models:

| Platform | What's Accessible | Key Limitation |
| :---- | :---- | :---- |
| YouTube | Content metadata, analytics, revenue data (3 APIs) | 10K query/day quota; 72-hr revenue delay |
| TikTok | Data Portability API exists | EEA/UK users only — US creators excluded |
| Instagram | Business/Creator accounts via Graph API | Basic Display API deprecated Dec 2024; no follower export |
| Twitch | Real-time stream data | Cannot retrieve historical per-stream analytics after broadcast |
| Patreon | Campaign and member data | No public analytics endpoint |
| Substack | Dashboard CSV export only | No API; migrating paid subscribers loses 5-15% |
| Midjourney | None | No official API — operates through Discord only |
| DALL-E / OpenAI | C2PA manifests on output files | Prompts not included in exported metadata |
| Runway | MP4 export (ProRes on Pro plans) | No generation parameters in metadata |
| ElevenLabs | Comprehensive REST API | Voice clone models cannot be exported — platform-locked |

## **The Metadata Stripping Problem**

| Critical constraint: Social media platforms systematically destroy metadata on upload. Facebook, Instagram, TikTok, and X strip EXIF, IPTC, XMP, PNG text chunks, and C2PA manifests during image processing. Only pixel-level watermarks like Google's SynthID survive platform recompression. |
| :---- |

This creates a fundamental architectural constraint: a portability engine must capture metadata before content enters social platforms, because retrieval after upload is impossible. The highest-value architecture is a prospective capture layer that intercepts content at creation time — not a retrospective archive tool. That is a harder product to build.

## **What the Remaining 30-40% Custom Build Looks Like**

* Platform-specific API adapters (ongoing maintenance as platforms change auth flows, deprecate endpoints, tighten rate limits)

* Creator-specific data models: prompt history, generation parameters, audience analytics, revenue records, deal data — none of this exists in DTP's consumer-oriented canonical models

* Creative asset schema: extending C2PA \+ IPTC 2025.1 to bundle content, provenance chain, creator identity, licensing terms, and version history in a single portable container

* Unified UI/UX for the vault dashboard and export flows

* The metadata capture layer — the hardest architectural piece

# **Build Complexity and Cost**

## **Team and Timeline Estimate**

A realistic MVP covering the top 10 platforms and AI tools requires a team of 6-8 engineers working 12-18 months:

| Role | Focus | Ongoing Load |
| :---- | :---- | :---- |
| 2x Senior Backend Engineers | Platform API integrations and data pipelines | High — platforms constantly change |
| 1x Data / Schema Engineer | Unified data model, ETL pipelines, metadata normalization | Medium |
| 1x Senior Frontend Engineer | Vault dashboard and export interface | Medium |
| 1x DevOps / Infrastructure | Cloud deployment, storage, security | Medium |
| 1x Security / Compliance | OAuth flows, GDPR, platform ToS review | High — legal exposure is real |

| Cost Component | Estimate |
| :---- | :---- |
| Annual team cost (US-based) | $1.2M \- $1.6M |
| Annual team cost (distributed) | $600K \- $900K |
| Legal review — platform ToS compliance | $50K \- $100K |
| Cloud infrastructure (scales with users) | $5K \- $15K / month |
| Year 1 all-in (lean distributed team) | $800K \- $1.5M |
| Year 1 all-in (US-based team) | $1.5M \- $2.5M |

| Open-source leverage: The C2PA SDKs alone save an estimated 6-12 months of custom provenance work. FFmpeg, ImageMagick, and ExifTool eliminate all conversion and metadata manipulation infrastructure. The estimated build-time reduction from leveraging existing open source is 60-70% of core infrastructure. |
| :---- |

The key ongoing risk is platform API instability. Every connector requires continuous maintenance. This is not a build-once problem — it is a permanent operational tax that scales linearly with the number of supported platforms.

# **Competitive Landscape**

## **What Exists**

No company has built exactly this product for creators. The closest analog is Spikerz (Tel Aviv), which raised $8.5M in seed funding (January 2025, led by Disruptive AI) for hack prevention, impersonator takedown, and content backup across Instagram, TikTok, YouTube, X, Facebook, and LinkedIn. Spikerz has 5,000+ brands and creators — but content backup is a secondary feature, not the core product.

| Company | What They Are | Gap vs. Creator Vault |
| :---- | :---- | :---- |
| Spikerz ($8.5M seed, 2025\) | Social media security \+ content backup | Backup is secondary; no portability or format conversion |
| SocialSafe (Hop-on Inc / OTC: HPNN) | DRM-protected social archive | Questionable execution capacity; no metadata layer |
| Social Archiver | Chrome extension, indie | Manual and limited; no AI tool support |
| Backupify (Datto/Kaseya) | Enterprise SaaS backup | Enterprise-only; no creator stack; no AI tools |
| CloudConvert / Zamzar | File format converters | No metadata, analytics, or business data — just files |

## **Comparable Pricing Models**

| Company | Model | Price Point |
| :---- | :---- | :---- |
| CloudConvert | Credit per conversion | Freemium; $14-$270/month enterprise |
| Zamzar | Freemium file conversion | $18-$70/month |
| BitTitan MigrationWiz | Per-user or per-10GB enterprise migration | $15-$30/user |
| Movebot | Per-GB data migration | $0.75/GB |
| Frame.io (Adobe) | Video collaboration per-seat | $15-$25/user/month |
| Egnyte | Enterprise content governance | $10-$46/user/month |

# **Business Model and Market Size**

## **Revenue Model for a Creator Portability Product**

| Tier | Target | Price | Value Prop |
| :---- | :---- | :---- | :---- |
| Creator Basic | Individual creators, $15K+ annual earnings | $9-$15/month | Automated backup, basic format conversion, vault access |
| Creator Pro | Full-time prosumer creators | $25-$39/month | Unlimited backup, full metadata preservation, batch migration |
| Agency / MCN | Agencies and MCNs managing creator rosters | $99-$299/month | Multi-account management, API access, compliance reporting |
| B2B Compliance | DMA-regulated platforms (Alphabet, Meta, TikTok) | Enterprise license | Portability-as-a-service to meet DMA/DMCCA mandates |

## **Market Size Assessment**

The professional creator segment — those earning over $15,000 annually — numbers roughly 2-4 million globally. Full-time creators use an average of 3.4 platforms, creating genuine fragmentation pain. 77% of creators report serious income risk from algorithm changes.

| Market Segment | Basis | Revenue Estimate |
| :---- | :---- | :---- |
| Professional creators (5-10% adoption @ $20/mo avg) | 2-4M creators, 5-10% penetration | $48-96M/year |
| Agency / MCN accounts | 500-2,000 accounts @ $200-500/month | $12-24M/year |
| B2B compliance licensing | DMA enforcement, EU AI Act, UK DMCCA | TBD — regulatory-driven |
| Total SAM (creator-facing) | Conservative estimate | $150-400M |
| Enterprise DAM market (adjacent) | Creator-specific DAM niche | $6.2B total, growing 15% CAGR |

| Market reality: The $150-400M SAM is real but not massive for a standalone venture-scale business. No funded startup has successfully built this as a standalone product — which likely reflects market reality rather than lack of vision. |
| :---- |

## **Regulatory Tailwinds**

The compliance landscape is accelerating demand:

* EU Digital Markets Act (DMA) — enforceable since March 2024\. Requires gatekeepers (Alphabet, Apple, Meta, Amazon, Microsoft, ByteDance) to provide continuous, real-time data access under Articles 6(9) and 6(10). Fines up to 6% of global turnover.

* UK Digital Markets, Competition and Consumers Act 2024 — CMA can mandate portability interventions with fines up to 10% of global annual turnover.

* Utah Digital Choice Act — effective July 2026, the first US state mandate for social media data portability.

* EU AI Act Article 50 — effective August 2026, requires AI-generated content marked in machine-readable, interoperable formats.

* Congressional Creators Caucus (formed June 2025\) \+ H.Res.1005 (Creator Bill of Rights) — calling for algorithmic transparency and data access rights.

# **Strategic Recommendation**

## **Module vs. Standalone**

The honest assessment: creator data portability is a feature-weight problem at seed stage, not a company-weight problem. The technical lift is manageable but the ongoing platform API maintenance burden is heavy, the standalone TAM is modest, and there is limited defensible moat once built. Platform adapters are maintenance-intensive but not technically unique.

The differentiation from generic converters would rest on three things:

* Creator-specific metadata preservation — prompts, generation parameters, audience analytics, revenue history — not just file format conversion

* A unified provenance chain using C2PA \+ IPTC tracking assets from creation through distribution

* The relationship and business data layer — deals, subscriber lists, platform relationships — that no file converter touches

| Recommended path: Build the portability engine as a core module within StudioYou rather than as a standalone product. This gives the technology a distribution channel, embeds it in a broader value proposition that justifies ongoing subscription revenue, and positions portability as infrastructure that creates StudioYou lock-in. The B2B compliance licensing play (selling portability-as-a-service to DMA-regulated platforms) can operate as a separate revenue stream regardless. |
| :---- |

For a seed-stage team, the recommended execution order: build the vault/archive infrastructure and the first 3-4 platform connectors (YouTube, Instagram, TikTok, one AI tool) as an integrated StudioYou module. Validate creator willingness to pay within that context. If the portability module shows strong standalone pull, it can be spun out. If not, it is still a powerful differentiator for the core platform.

## **The Spikerz Signal**

Spikerz's $8.5M seed raise proves investors see creator data protection as a real category — but notably, even Spikerz wraps portability inside a broader security value proposition rather than selling it standalone. That is the right structural instinct. The portability engine as StudioYou's core infrastructure: deploy it that way, own the creator data sovereignty story, and let the B2B compliance opportunity develop on its own timeline as DMA enforcement matures.

StudioYou — Confidential  |  SuperCreativePeople  |  lee@supercreativepeople.com  |  studioyou.studio

*This document is for internal strategic use only and is not for distribution.*