--
-- PostgreSQL database dump
--

-- Dumped from database version 10.18 (Ubuntu 10.18-1.pgdg21.04+1)
-- Dumped by pg_dump version 10.18 (Ubuntu 10.18-1.pgdg21.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: account_account; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.account_account (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    email character varying(60) NOT NULL,
    first_name character varying(60) NOT NULL,
    last_name character varying(60) NOT NULL,
    username character varying(60) NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_admin boolean NOT NULL,
    is_varified boolean NOT NULL,
    is_rejected boolean NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    gender character varying(10) NOT NULL,
    mobile character varying(10) NOT NULL
);


--
-- Name: account_account_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.account_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: account_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.account_account_id_seq OWNED BY public.account_account.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: cart_cart; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cart_cart (
    id bigint NOT NULL,
    cart_id character varying(50) NOT NULL,
    date_added date NOT NULL
);


--
-- Name: cart_cart_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cart_cart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cart_cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart_cart.id;


--
-- Name: cart_cartitem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cart_cartitem (
    id bigint NOT NULL,
    quantity integer NOT NULL,
    is_active boolean NOT NULL,
    cart_id bigint,
    user_id bigint,
    varient_id bigint NOT NULL
);


--
-- Name: cart_cartitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cart_cartitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cart_cartitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cart_cartitem_id_seq OWNED BY public.cart_cartitem.id;


--
-- Name: category_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.category_category (
    id bigint NOT NULL,
    category_name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    cat_image character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.category_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.category_category_id_seq OWNED BY public.category_category.id;


--
-- Name: category_sub_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.category_sub_category (
    id bigint NOT NULL,
    sub_category_name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    category_id bigint NOT NULL
);


--
-- Name: category_sub_category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.category_sub_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: category_sub_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.category_sub_category_id_seq OWNED BY public.category_sub_category.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: offer_categoryoffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_categoryoffer (
    id bigint NOT NULL,
    offer integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_valid boolean NOT NULL,
    category_name_id bigint NOT NULL
);


--
-- Name: offer_categoryoffer_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_categoryoffer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_categoryoffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_categoryoffer_id_seq OWNED BY public.offer_categoryoffer.id;


--
-- Name: offer_coupen; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_coupen (
    id bigint NOT NULL,
    coupen_code character varying(100) NOT NULL,
    coupen_count integer NOT NULL,
    valid_from date NOT NULL,
    valid_to date NOT NULL,
    discount integer NOT NULL,
    is_active boolean NOT NULL,
    created_at timestamp with time zone NOT NULL
);


--
-- Name: offer_coupen_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_coupen_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_coupen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_coupen_id_seq OWNED BY public.offer_coupen.id;


--
-- Name: offer_productoffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_productoffer (
    id bigint NOT NULL,
    offer integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_valid boolean NOT NULL,
    product_name_id bigint NOT NULL
);


--
-- Name: offer_productoffer_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_productoffer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_productoffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_productoffer_id_seq OWNED BY public.offer_productoffer.id;


--
-- Name: offer_redeemedcoupen; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_redeemedcoupen (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    coupen_id bigint NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: offer_redeemedcoupen_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_redeemedcoupen_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_redeemedcoupen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_redeemedcoupen_id_seq OWNED BY public.offer_redeemedcoupen.id;


--
-- Name: offer_subcategoryoffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_subcategoryoffer (
    id bigint NOT NULL,
    offer integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_valid boolean NOT NULL,
    subcategory_name_id bigint NOT NULL
);


--
-- Name: offer_subcategoryoffer_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_subcategoryoffer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_subcategoryoffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_subcategoryoffer_id_seq OWNED BY public.offer_subcategoryoffer.id;


--
-- Name: offer_variationoffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_variationoffer (
    id bigint NOT NULL,
    offer integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_valid boolean NOT NULL,
    variation_name_id bigint NOT NULL
);


--
-- Name: offer_variationoffer_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_variationoffer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_variationoffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_variationoffer_id_seq OWNED BY public.offer_variationoffer.id;


--
-- Name: offer_vendoroffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.offer_vendoroffer (
    id bigint NOT NULL,
    offer integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    is_valid boolean NOT NULL,
    vendor_name_id bigint NOT NULL
);


--
-- Name: offer_vendoroffer_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.offer_vendoroffer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: offer_vendoroffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.offer_vendoroffer_id_seq OWNED BY public.offer_vendoroffer.id;


--
-- Name: order_order; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.order_order (
    id bigint NOT NULL,
    order_number character varying(100) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone character varying(15) NOT NULL,
    email character varying(100) NOT NULL,
    address1 character varying(100) NOT NULL,
    address2 character varying(100) NOT NULL,
    country character varying(50) NOT NULL,
    state character varying(100) NOT NULL,
    city character varying(100) NOT NULL,
    pincode integer NOT NULL,
    order_note character varying(200) NOT NULL,
    order_total double precision NOT NULL,
    tax double precision NOT NULL,
    coupon_redeemed integer,
    status character varying(20) NOT NULL,
    ip character varying(20) NOT NULL,
    is_ordered boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    payment_id bigint,
    user_id bigint
);


--
-- Name: order_order_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.order_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: order_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.order_order_id_seq OWNED BY public.order_order.id;


--
-- Name: order_orderproduct; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.order_orderproduct (
    id bigint NOT NULL,
    status character varying(20) NOT NULL,
    quantity integer NOT NULL,
    price double precision NOT NULL,
    test character varying(100) NOT NULL,
    ordered boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    order_id bigint NOT NULL,
    payment_id bigint,
    products_id bigint NOT NULL,
    user_id bigint NOT NULL,
    variation_id bigint NOT NULL,
    vendor_id bigint NOT NULL
);


--
-- Name: order_orderproduct_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.order_orderproduct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: order_orderproduct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.order_orderproduct_id_seq OWNED BY public.order_orderproduct.id;


--
-- Name: order_payment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.order_payment (
    id bigint NOT NULL,
    payment_id character varying(100) NOT NULL,
    payment_method character varying(100) NOT NULL,
    amount_paid character varying(100) NOT NULL,
    status character varying(100) NOT NULL,
    created_at date NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: order_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.order_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: order_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.order_payment_id_seq OWNED BY public.order_payment.id;


--
-- Name: store_banners; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.store_banners (
    id bigint NOT NULL,
    name character varying(100),
    vendor_id bigint NOT NULL
);


--
-- Name: store_banners_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.store_banners_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: store_banners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.store_banners_id_seq OWNED BY public.store_banners.id;


--
-- Name: store_product; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.store_product (
    id bigint NOT NULL,
    product_name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    description text NOT NULL,
    image character varying(100) NOT NULL,
    is_available boolean NOT NULL,
    created_at time without time zone NOT NULL,
    updated_at time without time zone NOT NULL,
    category_id bigint NOT NULL,
    vendor_id bigint NOT NULL
);


--
-- Name: store_product_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.store_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: store_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.store_product_id_seq OWNED BY public.store_product.id;


--
-- Name: store_reviewrating; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.store_reviewrating (
    id bigint NOT NULL,
    subject character varying(100) NOT NULL,
    review text NOT NULL,
    rating double precision NOT NULL,
    ip character varying(20) NOT NULL,
    status boolean NOT NULL,
    created_at time without time zone NOT NULL,
    updated_at time without time zone NOT NULL,
    user_id bigint NOT NULL,
    varient_id bigint NOT NULL
);


--
-- Name: store_reviewrating_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.store_reviewrating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: store_reviewrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.store_reviewrating_id_seq OWNED BY public.store_reviewrating.id;


--
-- Name: store_variation; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.store_variation (
    id bigint NOT NULL,
    varient_name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    ram character varying(20) NOT NULL,
    storage character varying(50) NOT NULL,
    image4 character varying(100) NOT NULL,
    image1 character varying(100) NOT NULL,
    image2 character varying(100) NOT NULL,
    image3 character varying(100) NOT NULL,
    margin_price integer NOT NULL,
    price integer NOT NULL,
    stock integer NOT NULL,
    is_available boolean NOT NULL,
    created_at time without time zone NOT NULL,
    updated_at time without time zone NOT NULL,
    color_id bigint NOT NULL,
    product_id bigint NOT NULL
);


--
-- Name: store_variation_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.store_variation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: store_variation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.store_variation_id_seq OWNED BY public.store_variation.id;


--
-- Name: store_varientcolor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.store_varientcolor (
    id bigint NOT NULL,
    color_name character varying(50) NOT NULL
);


--
-- Name: store_varientcolor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.store_varientcolor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: store_varientcolor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.store_varientcolor_id_seq OWNED BY public.store_varientcolor.id;


--
-- Name: user_address; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_address (
    id bigint NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone character varying(15) NOT NULL,
    email character varying(100) NOT NULL,
    address1 character varying(100) NOT NULL,
    address2 character varying(100) NOT NULL,
    country character varying(50) NOT NULL,
    state character varying(100) NOT NULL,
    city character varying(100) NOT NULL,
    pincode integer NOT NULL,
    add_type character varying(50) NOT NULL,
    user_id bigint
);


--
-- Name: user_address_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_address_id_seq OWNED BY public.user_address.id;


--
-- Name: user_profile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profile (
    id bigint NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    gender character varying(10),
    phone character varying(15) NOT NULL,
    email character varying(100) NOT NULL,
    profile_picture character varying(100) NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: user_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profile_id_seq OWNED BY public.user_profile.id;


--
-- Name: vendors_vendors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.vendors_vendors (
    vendor_id_id bigint NOT NULL,
    brand_name character varying(60) NOT NULL,
    tagline character varying(200) NOT NULL,
    logo character varying(100) NOT NULL,
    description text NOT NULL
);


--
-- Name: account_account id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.account_account ALTER COLUMN id SET DEFAULT nextval('public.account_account_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: cart_cart id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cart ALTER COLUMN id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);


--
-- Name: cart_cartitem id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem ALTER COLUMN id SET DEFAULT nextval('public.cart_cartitem_id_seq'::regclass);


--
-- Name: category_category id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_category ALTER COLUMN id SET DEFAULT nextval('public.category_category_id_seq'::regclass);


--
-- Name: category_sub_category id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_sub_category ALTER COLUMN id SET DEFAULT nextval('public.category_sub_category_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: offer_categoryoffer id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_categoryoffer ALTER COLUMN id SET DEFAULT nextval('public.offer_categoryoffer_id_seq'::regclass);


--
-- Name: offer_coupen id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_coupen ALTER COLUMN id SET DEFAULT nextval('public.offer_coupen_id_seq'::regclass);


--
-- Name: offer_productoffer id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_productoffer ALTER COLUMN id SET DEFAULT nextval('public.offer_productoffer_id_seq'::regclass);


--
-- Name: offer_redeemedcoupen id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_redeemedcoupen ALTER COLUMN id SET DEFAULT nextval('public.offer_redeemedcoupen_id_seq'::regclass);


--
-- Name: offer_subcategoryoffer id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_subcategoryoffer ALTER COLUMN id SET DEFAULT nextval('public.offer_subcategoryoffer_id_seq'::regclass);


--
-- Name: offer_variationoffer id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_variationoffer ALTER COLUMN id SET DEFAULT nextval('public.offer_variationoffer_id_seq'::regclass);


--
-- Name: offer_vendoroffer id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_vendoroffer ALTER COLUMN id SET DEFAULT nextval('public.offer_vendoroffer_id_seq'::regclass);


--
-- Name: order_order id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_order ALTER COLUMN id SET DEFAULT nextval('public.order_order_id_seq'::regclass);


--
-- Name: order_orderproduct id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct ALTER COLUMN id SET DEFAULT nextval('public.order_orderproduct_id_seq'::regclass);


--
-- Name: order_payment id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_payment ALTER COLUMN id SET DEFAULT nextval('public.order_payment_id_seq'::regclass);


--
-- Name: store_banners id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_banners ALTER COLUMN id SET DEFAULT nextval('public.store_banners_id_seq'::regclass);


--
-- Name: store_product id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_product ALTER COLUMN id SET DEFAULT nextval('public.store_product_id_seq'::regclass);


--
-- Name: store_reviewrating id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_reviewrating ALTER COLUMN id SET DEFAULT nextval('public.store_reviewrating_id_seq'::regclass);


--
-- Name: store_variation id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_variation ALTER COLUMN id SET DEFAULT nextval('public.store_variation_id_seq'::regclass);


--
-- Name: store_varientcolor id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_varientcolor ALTER COLUMN id SET DEFAULT nextval('public.store_varientcolor_id_seq'::regclass);


--
-- Name: user_address id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_address ALTER COLUMN id SET DEFAULT nextval('public.user_address_id_seq'::regclass);


--
-- Name: user_profile id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile ALTER COLUMN id SET DEFAULT nextval('public.user_profile_id_seq'::regclass);


--
-- Data for Name: account_account; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.account_account (id, password, email, first_name, last_name, username, date_joined, last_login, is_admin, is_varified, is_rejected, is_active, is_staff, is_superuser, gender, mobile) FROM stdin;
3	pbkdf2_sha256$260000$QR72YLvuzy695wFx6KZ5eV$A199tAak5dCMZPVbnbB/cf7hw1+YyNYYZkhZKwHHElk=	apple@gmail.com	Apple			2021-12-12 01:01:16.881334+05:30	2021-12-12 01:01:16.881351+05:30	f	t	f	t	t	f		7907881989
1	pbkdf2_sha256$260000$HJalXiDffMf1mN0it7ktkl$/Tl1qCehJNxfKQcbUVTCO9y1jEzA9gbbOxZIFHjd6XI=	mfayisam@gmail.com	mohmd	faiz		2021-12-11 23:56:49.298191+05:30	2021-12-12 10:38:52.333541+05:30	t	t	f	t	t	t		7907881989
2	pbkdf2_sha256$260000$RHBeJGssPwiqJg2fh73JnN$cwCHlCZ/RlP1BB1KqfYIhy/KQyzjLUVDQcQyhCEmunA=	samsung@gmail.com	SAMSUNG			2021-12-12 00:59:04.904134+05:30	2021-12-12 10:51:38.181259+05:30	f	t	f	t	t	f		8086947995
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add profile	6	add_profile
22	Can change profile	6	change_profile
23	Can delete profile	6	delete_profile
24	Can view profile	6	view_profile
25	Can add address	7	add_address
26	Can change address	7	change_address
27	Can delete address	7	delete_address
28	Can view address	7	view_address
29	Can add account	8	add_account
30	Can change account	8	change_account
31	Can delete account	8	delete_account
32	Can view account	8	view_account
33	Can add vendors	9	add_vendors
34	Can change vendors	9	change_vendors
35	Can delete vendors	9	delete_vendors
36	Can view vendors	9	view_vendors
37	Can add category	10	add_category
38	Can change category	10	change_category
39	Can delete category	10	delete_category
40	Can view category	10	view_category
41	Can add sub_category	11	add_sub_category
42	Can change sub_category	11	change_sub_category
43	Can delete sub_category	11	delete_sub_category
44	Can view sub_category	11	view_sub_category
45	Can add product	12	add_product
46	Can change product	12	change_product
47	Can delete product	12	delete_product
48	Can view product	12	view_product
49	Can add varient color	13	add_varientcolor
50	Can change varient color	13	change_varientcolor
51	Can delete varient color	13	delete_varientcolor
52	Can view varient color	13	view_varientcolor
53	Can add variation	14	add_variation
54	Can change variation	14	change_variation
55	Can delete variation	14	delete_variation
56	Can view variation	14	view_variation
57	Can add review rating	15	add_reviewrating
58	Can change review rating	15	change_reviewrating
59	Can delete review rating	15	delete_reviewrating
60	Can view review rating	15	view_reviewrating
61	Can add banners	16	add_banners
62	Can change banners	16	change_banners
63	Can delete banners	16	delete_banners
64	Can view banners	16	view_banners
65	Can add cart	17	add_cart
66	Can change cart	17	change_cart
67	Can delete cart	17	delete_cart
68	Can view cart	17	view_cart
69	Can add cart item	18	add_cartitem
70	Can change cart item	18	change_cartitem
71	Can delete cart item	18	delete_cartitem
72	Can view cart item	18	view_cartitem
73	Can add order	19	add_order
74	Can change order	19	change_order
75	Can delete order	19	delete_order
76	Can view order	19	view_order
77	Can add payment	20	add_payment
78	Can change payment	20	change_payment
79	Can delete payment	20	delete_payment
80	Can view payment	20	view_payment
81	Can add order product	21	add_orderproduct
82	Can change order product	21	change_orderproduct
83	Can delete order product	21	delete_orderproduct
84	Can view order product	21	view_orderproduct
85	Can add coupen	22	add_coupen
86	Can change coupen	22	change_coupen
87	Can delete coupen	22	delete_coupen
88	Can view coupen	22	view_coupen
89	Can add vendor offer	23	add_vendoroffer
90	Can change vendor offer	23	change_vendoroffer
91	Can delete vendor offer	23	delete_vendoroffer
92	Can view vendor offer	23	view_vendoroffer
93	Can add variation offer	24	add_variationoffer
94	Can change variation offer	24	change_variationoffer
95	Can delete variation offer	24	delete_variationoffer
96	Can view variation offer	24	view_variationoffer
97	Can add sub category offer	25	add_subcategoryoffer
98	Can change sub category offer	25	change_subcategoryoffer
99	Can delete sub category offer	25	delete_subcategoryoffer
100	Can view sub category offer	25	view_subcategoryoffer
101	Can add redeemed coupen	26	add_redeemedcoupen
102	Can change redeemed coupen	26	change_redeemedcoupen
103	Can delete redeemed coupen	26	delete_redeemedcoupen
104	Can view redeemed coupen	26	view_redeemedcoupen
105	Can add product offer	27	add_productoffer
106	Can change product offer	27	change_productoffer
107	Can delete product offer	27	delete_productoffer
108	Can view product offer	27	view_productoffer
109	Can add category offer	28	add_categoryoffer
110	Can change category offer	28	change_categoryoffer
111	Can delete category offer	28	delete_categoryoffer
112	Can view category offer	28	view_categoryoffer
\.


--
-- Data for Name: cart_cart; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cart_cart (id, cart_id, date_added) FROM stdin;
\.


--
-- Data for Name: cart_cartitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cart_cartitem (id, quantity, is_active, cart_id, user_id, varient_id) FROM stdin;
\.


--
-- Data for Name: category_category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.category_category (id, category_name, slug, cat_image, created_at, updated_at) FROM stdin;
1	Premium Phones	premium-phones		2021-12-12 01:18:12.573822+05:30	2021-12-12 01:18:12.573847+05:30
2	Gaming Phones	gaming-phones		2021-12-12 01:18:24.655504+05:30	2021-12-12 01:18:24.65553+05:30
3	Mid Range Phones	mid-range-phones		2021-12-12 01:18:53.213597+05:30	2021-12-12 01:18:53.213625+05:30
\.


--
-- Data for Name: category_sub_category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.category_sub_category (id, sub_category_name, slug, created_at, updated_at, category_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-12-12 02:14:07.036706+05:30	1	BLACK	1	[{"added": {}}]	13	1
2	2021-12-12 02:14:11.518255+05:30	2	RED	1	[{"added": {}}]	13	1
3	2021-12-12 02:14:18.14057+05:30	3	BLUE	1	[{"added": {}}]	13	1
4	2021-12-12 02:14:22.966401+05:30	4	GREEN	1	[{"added": {}}]	13	1
5	2021-12-12 02:14:27.406915+05:30	5	GREY	1	[{"added": {}}]	13	1
6	2021-12-12 02:14:30.84728+05:30	6	WHITE	1	[{"added": {}}]	13	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	user	profile
7	user	address
8	account	account
9	vendors	vendors
10	category	category
11	category	sub_category
12	store	product
13	store	varientcolor
14	store	variation
15	store	reviewrating
16	store	banners
17	cart	cart
18	cart	cartitem
19	order	order
20	order	payment
21	order	orderproduct
22	offer	coupen
23	offer	vendoroffer
24	offer	variationoffer
25	offer	subcategoryoffer
26	offer	redeemedcoupen
27	offer	productoffer
28	offer	categoryoffer
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	account	0001_initial	2021-12-11 23:54:58.595572+05:30
2	contenttypes	0001_initial	2021-12-11 23:54:58.702738+05:30
3	admin	0001_initial	2021-12-11 23:54:58.879584+05:30
4	admin	0002_logentry_remove_auto_add	2021-12-11 23:54:58.905849+05:30
5	admin	0003_logentry_add_action_flag_choices	2021-12-11 23:54:58.926521+05:30
6	contenttypes	0002_remove_content_type_name	2021-12-11 23:54:58.957102+05:30
7	auth	0001_initial	2021-12-11 23:54:59.885282+05:30
8	auth	0002_alter_permission_name_max_length	2021-12-11 23:54:59.952828+05:30
9	auth	0003_alter_user_email_max_length	2021-12-11 23:54:59.977153+05:30
10	auth	0004_alter_user_username_opts	2021-12-11 23:55:00.007956+05:30
11	auth	0005_alter_user_last_login_null	2021-12-11 23:55:00.040699+05:30
12	auth	0006_require_contenttypes_0002	2021-12-11 23:55:00.068261+05:30
13	auth	0007_alter_validators_add_error_messages	2021-12-11 23:55:00.104707+05:30
14	auth	0008_alter_user_username_max_length	2021-12-11 23:55:00.138337+05:30
15	auth	0009_alter_user_last_name_max_length	2021-12-11 23:55:00.170737+05:30
16	auth	0010_alter_group_name_max_length	2021-12-11 23:55:00.207184+05:30
17	auth	0011_update_proxy_permissions	2021-12-11 23:55:00.240348+05:30
18	auth	0012_alter_user_first_name_max_length	2021-12-11 23:55:00.269253+05:30
19	vendors	0001_initial	2021-12-11 23:55:00.531828+05:30
20	category	0001_initial	2021-12-11 23:55:01.436475+05:30
21	store	0001_initial	2021-12-11 23:55:03.638403+05:30
22	cart	0001_initial	2021-12-11 23:55:04.121949+05:30
23	offer	0001_initial	2021-12-11 23:55:06.931997+05:30
24	order	0001_initial	2021-12-11 23:55:09.087361+05:30
25	sessions	0001_initial	2021-12-11 23:55:09.416791+05:30
26	user	0001_initial	2021-12-11 23:55:09.956933+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
qjmfx58maqkq8q9a6fgkn69y4gdt86r3	e30:1mw8QV:JtIfukKveK-plWrTpt3rbOy4-Cr1vCSUkmiZBENyp_U	2021-12-26 01:22:59.36631+05:30
dn1od7s1nwiinv7oleyk1tp4mvrdin4l	.eJxVjMsOwiAQRf-FtSHlDS7d-w1khgGpGkhKuzL-uzbpQrf3nHNfLMK21riNvMSZ2JkJdvrdENIjtx3QHdqt89TbuszId4UfdPBrp_y8HO7fQYVRv7UuGJwKwVMC7dBMQGDUpANY5Yr1WNApjVYCJnBSOAJhZBaUvMlKIHt_AOo3OCw:1mw8V1:7M7hlUiwvaq-a7o_kjFDqKEHpai_ewxdRiIuVyYcBY0	2021-12-26 01:27:39.269211+05:30
rdr8y1lci80jo0zhwd5i3ctkw1xyzgwk	.eJxVjEEOwiAQRe_C2hCYdii4dO8ZyAxQqRpISrsy3l1JutDte-__l_C0b9nvLa1-ieIsQJx-GVN4pNJFvFO5VRlq2daFZU_kYZu81piel6P9O8jUcl8jMTgzxKgJSYNRoEYTpkCWAZDGpBG0cxj08KVqVtYGnBIyqwh2Fu8P1N43iQ:1mw96t:WsLEmAIK9p294EvJIwnxa9TFcXdFxZy5Z1dIvbwFdH0	2021-12-26 02:06:47.692093+05:30
z7b5w8pztby68tvgfh6jnt5lsu8uwmdn	.eJxVjMsOwiAQRf-FtSHlDS7d-w1khgGpGkhKuzL-uzbpQrf3nHNfLMK21riNvMSZ2JkJdvrdENIjtx3QHdqt89TbuszId4UfdPBrp_y8HO7fQYVRv7UuGJwKwVMC7dBMQGDUpANY5Yr1WNApjVYCJnBSOAJhZBaUvMlKIHt_AOo3OCw:1mw9Dc:alJRkyF5K8sKFMohHP71MfgvXYp0k7ypkv5fo2Hmzlk	2021-12-26 02:13:44.118959+05:30
4e37gvhmy9i5wl18md30i55qdl7byu5j	.eJxVjEEOwiAQRe_C2hCYdii4dO8ZyAxQqRpISrsy3l1JutDte-__l_C0b9nvLa1-ieIsQJx-GVN4pNJFvFO5VRlq2daFZU_kYZu81piel6P9O8jUcl8jMTgzxKgJSYNRoEYTpkCWAZDGpBG0cxj08KVqVtYGnBIyqwh2Fu8P1N43iQ:1mwHIo:geP_eotIsHCwJITDEEmg05ExV82bC-3onCBEqiUm_Pk	2021-12-26 10:51:38.203703+05:30
\.


--
-- Data for Name: offer_categoryoffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_categoryoffer (id, offer, created_at, modified_at, is_valid, category_name_id) FROM stdin;
\.


--
-- Data for Name: offer_coupen; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_coupen (id, coupen_code, coupen_count, valid_from, valid_to, discount, is_active, created_at) FROM stdin;
\.


--
-- Data for Name: offer_productoffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_productoffer (id, offer, created_at, modified_at, is_valid, product_name_id) FROM stdin;
\.


--
-- Data for Name: offer_redeemedcoupen; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_redeemedcoupen (id, created_at, coupen_id, user_id) FROM stdin;
\.


--
-- Data for Name: offer_subcategoryoffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_subcategoryoffer (id, offer, created_at, modified_at, is_valid, subcategory_name_id) FROM stdin;
\.


--
-- Data for Name: offer_variationoffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_variationoffer (id, offer, created_at, modified_at, is_valid, variation_name_id) FROM stdin;
\.


--
-- Data for Name: offer_vendoroffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.offer_vendoroffer (id, offer, created_at, modified_at, is_valid, vendor_name_id) FROM stdin;
\.


--
-- Data for Name: order_order; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.order_order (id, order_number, first_name, last_name, phone, email, address1, address2, country, state, city, pincode, order_note, order_total, tax, coupon_redeemed, status, ip, is_ordered, created_at, updated_at, payment_id, user_id) FROM stdin;
\.


--
-- Data for Name: order_orderproduct; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.order_orderproduct (id, status, quantity, price, test, ordered, created_at, updated_at, order_id, payment_id, products_id, user_id, variation_id, vendor_id) FROM stdin;
\.


--
-- Data for Name: order_payment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.order_payment (id, payment_id, payment_method, amount_paid, status, created_at, user_id) FROM stdin;
\.


--
-- Data for Name: store_banners; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.store_banners (id, name, vendor_id) FROM stdin;
\.


--
-- Data for Name: store_product; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.store_product (id, product_name, slug, description, image, is_available, created_at, updated_at, category_id, vendor_id) FROM stdin;
1	Galaxy S20	galaxy-s20			t	19:56:05.951016	19:56:05.951028	1	2
\.


--
-- Data for Name: store_reviewrating; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.store_reviewrating (id, subject, review, rating, ip, status, created_at, updated_at, user_id, varient_id) FROM stdin;
\.


--
-- Data for Name: store_variation; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.store_variation (id, varient_name, slug, ram, storage, image4, image1, image2, image3, margin_price, price, stock, is_available, created_at, updated_at, color_id, product_id) FROM stdin;
1	qwert	kjbkb	2 GB	32 GB	photos/product/product-6_YEr0agj.jpg	photos/product/html.png	photos/product/logo.png	photos/product/Mumbai_Skyline_at_Night.jpg	485	646	48	t	20:49:33.844309	20:49:33.844325	3	1
\.


--
-- Data for Name: store_varientcolor; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.store_varientcolor (id, color_name) FROM stdin;
1	BLACK
2	RED
3	BLUE
4	GREEN
5	GREY
6	WHITE
\.


--
-- Data for Name: user_address; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_address (id, first_name, last_name, phone, email, address1, address2, country, state, city, pincode, add_type, user_id) FROM stdin;
\.


--
-- Data for Name: user_profile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_profile (id, first_name, last_name, gender, phone, email, profile_picture, user_id) FROM stdin;
\.


--
-- Data for Name: vendors_vendors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.vendors_vendors (vendor_id_id, brand_name, tagline, logo, description) FROM stdin;
2	SAMSUNG	Samsung, Turn on Tomorrow. Samsung, The Next Is Now. Samsung, The Next Big Thing is Here. Do bigger things.		descf
\.


--
-- Name: account_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.account_account_id_seq', 3, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 112, true);


--
-- Name: cart_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cart_cart_id_seq', 1, false);


--
-- Name: cart_cartitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cart_cartitem_id_seq', 1, false);


--
-- Name: category_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.category_category_id_seq', 3, true);


--
-- Name: category_sub_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.category_sub_category_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 6, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 28, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: offer_categoryoffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_categoryoffer_id_seq', 1, false);


--
-- Name: offer_coupen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_coupen_id_seq', 1, false);


--
-- Name: offer_productoffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_productoffer_id_seq', 1, false);


--
-- Name: offer_redeemedcoupen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_redeemedcoupen_id_seq', 1, false);


--
-- Name: offer_subcategoryoffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_subcategoryoffer_id_seq', 1, false);


--
-- Name: offer_variationoffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_variationoffer_id_seq', 1, false);


--
-- Name: offer_vendoroffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.offer_vendoroffer_id_seq', 1, false);


--
-- Name: order_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.order_order_id_seq', 1, false);


--
-- Name: order_orderproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.order_orderproduct_id_seq', 1, false);


--
-- Name: order_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.order_payment_id_seq', 1, false);


--
-- Name: store_banners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.store_banners_id_seq', 1, false);


--
-- Name: store_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.store_product_id_seq', 1, true);


--
-- Name: store_reviewrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.store_reviewrating_id_seq', 1, false);


--
-- Name: store_variation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.store_variation_id_seq', 1, true);


--
-- Name: store_varientcolor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.store_varientcolor_id_seq', 6, true);


--
-- Name: user_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_address_id_seq', 1, false);


--
-- Name: user_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_profile_id_seq', 1, false);


--
-- Name: account_account account_account_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.account_account
    ADD CONSTRAINT account_account_email_key UNIQUE (email);


--
-- Name: account_account account_account_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.account_account
    ADD CONSTRAINT account_account_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: cart_cart cart_cart_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_pkey PRIMARY KEY (id);


--
-- Name: cart_cartitem cart_cartitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_pkey PRIMARY KEY (id);


--
-- Name: category_category category_category_category_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_category
    ADD CONSTRAINT category_category_category_name_key UNIQUE (category_name);


--
-- Name: category_category category_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_category
    ADD CONSTRAINT category_category_pkey PRIMARY KEY (id);


--
-- Name: category_category category_category_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_category
    ADD CONSTRAINT category_category_slug_key UNIQUE (slug);


--
-- Name: category_sub_category category_sub_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_sub_category
    ADD CONSTRAINT category_sub_category_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: offer_categoryoffer offer_categoryoffer_category_name_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_categoryoffer
    ADD CONSTRAINT offer_categoryoffer_category_name_id_key UNIQUE (category_name_id);


--
-- Name: offer_categoryoffer offer_categoryoffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_categoryoffer
    ADD CONSTRAINT offer_categoryoffer_pkey PRIMARY KEY (id);


--
-- Name: offer_coupen offer_coupen_coupen_code_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_coupen
    ADD CONSTRAINT offer_coupen_coupen_code_key UNIQUE (coupen_code);


--
-- Name: offer_coupen offer_coupen_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_coupen
    ADD CONSTRAINT offer_coupen_pkey PRIMARY KEY (id);


--
-- Name: offer_productoffer offer_productoffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_productoffer
    ADD CONSTRAINT offer_productoffer_pkey PRIMARY KEY (id);


--
-- Name: offer_productoffer offer_productoffer_product_name_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_productoffer
    ADD CONSTRAINT offer_productoffer_product_name_id_key UNIQUE (product_name_id);


--
-- Name: offer_redeemedcoupen offer_redeemedcoupen_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_redeemedcoupen
    ADD CONSTRAINT offer_redeemedcoupen_pkey PRIMARY KEY (id);


--
-- Name: offer_subcategoryoffer offer_subcategoryoffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_subcategoryoffer
    ADD CONSTRAINT offer_subcategoryoffer_pkey PRIMARY KEY (id);


--
-- Name: offer_subcategoryoffer offer_subcategoryoffer_subcategory_name_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_subcategoryoffer
    ADD CONSTRAINT offer_subcategoryoffer_subcategory_name_id_key UNIQUE (subcategory_name_id);


--
-- Name: offer_variationoffer offer_variationoffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_variationoffer
    ADD CONSTRAINT offer_variationoffer_pkey PRIMARY KEY (id);


--
-- Name: offer_variationoffer offer_variationoffer_variation_name_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_variationoffer
    ADD CONSTRAINT offer_variationoffer_variation_name_id_key UNIQUE (variation_name_id);


--
-- Name: offer_vendoroffer offer_vendoroffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_vendoroffer
    ADD CONSTRAINT offer_vendoroffer_pkey PRIMARY KEY (id);


--
-- Name: offer_vendoroffer offer_vendoroffer_vendor_name_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_vendoroffer
    ADD CONSTRAINT offer_vendoroffer_vendor_name_id_key UNIQUE (vendor_name_id);


--
-- Name: order_order order_order_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_order
    ADD CONSTRAINT order_order_pkey PRIMARY KEY (id);


--
-- Name: order_orderproduct order_orderproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_pkey PRIMARY KEY (id);


--
-- Name: order_payment order_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_payment
    ADD CONSTRAINT order_payment_pkey PRIMARY KEY (id);


--
-- Name: store_banners store_banners_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_banners
    ADD CONSTRAINT store_banners_pkey PRIMARY KEY (id);


--
-- Name: store_product store_product_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_product
    ADD CONSTRAINT store_product_pkey PRIMARY KEY (id);


--
-- Name: store_reviewrating store_reviewrating_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_reviewrating
    ADD CONSTRAINT store_reviewrating_pkey PRIMARY KEY (id);


--
-- Name: store_variation store_variation_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_variation
    ADD CONSTRAINT store_variation_pkey PRIMARY KEY (id);


--
-- Name: store_varientcolor store_varientcolor_color_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_varientcolor
    ADD CONSTRAINT store_varientcolor_color_name_key UNIQUE (color_name);


--
-- Name: store_varientcolor store_varientcolor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_varientcolor
    ADD CONSTRAINT store_varientcolor_pkey PRIMARY KEY (id);


--
-- Name: user_address user_address_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_address
    ADD CONSTRAINT user_address_pkey PRIMARY KEY (id);


--
-- Name: user_profile user_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile
    ADD CONSTRAINT user_profile_pkey PRIMARY KEY (id);


--
-- Name: user_profile user_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile
    ADD CONSTRAINT user_profile_user_id_key UNIQUE (user_id);


--
-- Name: vendors_vendors vendors_vendors_brand_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.vendors_vendors
    ADD CONSTRAINT vendors_vendors_brand_name_key UNIQUE (brand_name);


--
-- Name: vendors_vendors vendors_vendors_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.vendors_vendors
    ADD CONSTRAINT vendors_vendors_pkey PRIMARY KEY (vendor_id_id);


--
-- Name: account_account_email_3d3b3e7a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX account_account_email_3d3b3e7a_like ON public.account_account USING btree (email varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: cart_cartitem_cart_id_370ad265; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cart_cartitem_cart_id_370ad265 ON public.cart_cartitem USING btree (cart_id);


--
-- Name: cart_cartitem_user_id_292943b8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cart_cartitem_user_id_292943b8 ON public.cart_cartitem USING btree (user_id);


--
-- Name: cart_cartitem_varient_id_433a3098; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cart_cartitem_varient_id_433a3098 ON public.cart_cartitem USING btree (varient_id);


--
-- Name: category_category_category_name_1aa3ee61_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_category_category_name_1aa3ee61_like ON public.category_category USING btree (category_name varchar_pattern_ops);


--
-- Name: category_category_slug_4f83d5f6_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_category_slug_4f83d5f6_like ON public.category_category USING btree (slug varchar_pattern_ops);


--
-- Name: category_sub_category_category_id_daa1d4d0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_sub_category_category_id_daa1d4d0 ON public.category_sub_category USING btree (category_id);


--
-- Name: category_sub_category_slug_38b4d217; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_sub_category_slug_38b4d217 ON public.category_sub_category USING btree (slug);


--
-- Name: category_sub_category_slug_38b4d217_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_sub_category_slug_38b4d217_like ON public.category_sub_category USING btree (slug varchar_pattern_ops);


--
-- Name: category_sub_category_sub_category_name_70d3f932; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_sub_category_sub_category_name_70d3f932 ON public.category_sub_category USING btree (sub_category_name);


--
-- Name: category_sub_category_sub_category_name_70d3f932_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX category_sub_category_sub_category_name_70d3f932_like ON public.category_sub_category USING btree (sub_category_name varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: offer_coupen_coupen_code_2f60eecb_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX offer_coupen_coupen_code_2f60eecb_like ON public.offer_coupen USING btree (coupen_code varchar_pattern_ops);


--
-- Name: offer_redeemedcoupen_coupen_id_3d43a381; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX offer_redeemedcoupen_coupen_id_3d43a381 ON public.offer_redeemedcoupen USING btree (coupen_id);


--
-- Name: offer_redeemedcoupen_user_id_1016b35d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX offer_redeemedcoupen_user_id_1016b35d ON public.offer_redeemedcoupen USING btree (user_id);


--
-- Name: order_order_payment_id_d8fb3a38; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_order_payment_id_d8fb3a38 ON public.order_order USING btree (payment_id);


--
-- Name: order_order_user_id_7cf9bc2b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_order_user_id_7cf9bc2b ON public.order_order USING btree (user_id);


--
-- Name: order_orderproduct_order_id_18dae3b0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_order_id_18dae3b0 ON public.order_orderproduct USING btree (order_id);


--
-- Name: order_orderproduct_payment_id_13b3c50a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_payment_id_13b3c50a ON public.order_orderproduct USING btree (payment_id);


--
-- Name: order_orderproduct_products_id_ee6c5f04; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_products_id_ee6c5f04 ON public.order_orderproduct USING btree (products_id);


--
-- Name: order_orderproduct_user_id_d5f4875a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_user_id_d5f4875a ON public.order_orderproduct USING btree (user_id);


--
-- Name: order_orderproduct_variation_id_2e3db5f4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_variation_id_2e3db5f4 ON public.order_orderproduct USING btree (variation_id);


--
-- Name: order_orderproduct_vendor_id_7c016ce6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_orderproduct_vendor_id_7c016ce6 ON public.order_orderproduct USING btree (vendor_id);


--
-- Name: order_payment_user_id_51d05b30; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX order_payment_user_id_51d05b30 ON public.order_payment USING btree (user_id);


--
-- Name: store_banners_vendor_id_6bbceeb2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_banners_vendor_id_6bbceeb2 ON public.store_banners USING btree (vendor_id);


--
-- Name: store_product_category_id_574bae65; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_product_category_id_574bae65 ON public.store_product USING btree (category_id);


--
-- Name: store_product_slug_6de8ee4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_product_slug_6de8ee4b ON public.store_product USING btree (slug);


--
-- Name: store_product_slug_6de8ee4b_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_product_slug_6de8ee4b_like ON public.store_product USING btree (slug varchar_pattern_ops);


--
-- Name: store_product_vendor_id_f9abf9af; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_product_vendor_id_f9abf9af ON public.store_product USING btree (vendor_id);


--
-- Name: store_reviewrating_user_id_da0ed849; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_reviewrating_user_id_da0ed849 ON public.store_reviewrating USING btree (user_id);


--
-- Name: store_reviewrating_varient_id_df5e34f2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_reviewrating_varient_id_df5e34f2 ON public.store_reviewrating USING btree (varient_id);


--
-- Name: store_variation_color_id_9a8c70b6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_variation_color_id_9a8c70b6 ON public.store_variation USING btree (color_id);


--
-- Name: store_variation_product_id_e4f08cbc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_variation_product_id_e4f08cbc ON public.store_variation USING btree (product_id);


--
-- Name: store_variation_slug_8d4ff863; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_variation_slug_8d4ff863 ON public.store_variation USING btree (slug);


--
-- Name: store_variation_slug_8d4ff863_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_variation_slug_8d4ff863_like ON public.store_variation USING btree (slug varchar_pattern_ops);


--
-- Name: store_varientcolor_color_name_398e63b2_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX store_varientcolor_color_name_398e63b2_like ON public.store_varientcolor USING btree (color_name varchar_pattern_ops);


--
-- Name: user_address_user_id_64deb2c7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_address_user_id_64deb2c7 ON public.user_address USING btree (user_id);


--
-- Name: vendors_vendors_brand_name_78e110cc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vendors_vendors_brand_name_78e110cc_like ON public.vendors_vendors USING btree (brand_name varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cartitem cart_cartitem_cart_id_370ad265_fk_cart_cart_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_cart_id_370ad265_fk_cart_cart_id FOREIGN KEY (cart_id) REFERENCES public.cart_cart(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cartitem cart_cartitem_user_id_292943b8_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_user_id_292943b8_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cartitem cart_cartitem_varient_id_433a3098_fk_store_variation_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_varient_id_433a3098_fk_store_variation_id FOREIGN KEY (varient_id) REFERENCES public.store_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: category_sub_category category_sub_categor_category_id_daa1d4d0_fk_category_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.category_sub_category
    ADD CONSTRAINT category_sub_categor_category_id_daa1d4d0_fk_category_ FOREIGN KEY (category_id) REFERENCES public.category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_categoryoffer offer_categoryoffer_category_name_id_2ef01155_fk_category_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_categoryoffer
    ADD CONSTRAINT offer_categoryoffer_category_name_id_2ef01155_fk_category_ FOREIGN KEY (category_name_id) REFERENCES public.category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_productoffer offer_productoffer_product_name_id_f2738b93_fk_store_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_productoffer
    ADD CONSTRAINT offer_productoffer_product_name_id_f2738b93_fk_store_product_id FOREIGN KEY (product_name_id) REFERENCES public.store_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_redeemedcoupen offer_redeemedcoupen_coupen_id_3d43a381_fk_offer_coupen_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_redeemedcoupen
    ADD CONSTRAINT offer_redeemedcoupen_coupen_id_3d43a381_fk_offer_coupen_id FOREIGN KEY (coupen_id) REFERENCES public.offer_coupen(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_redeemedcoupen offer_redeemedcoupen_user_id_1016b35d_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_redeemedcoupen
    ADD CONSTRAINT offer_redeemedcoupen_user_id_1016b35d_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_subcategoryoffer offer_subcategoryoff_subcategory_name_id_7f1df8f0_fk_category_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_subcategoryoffer
    ADD CONSTRAINT offer_subcategoryoff_subcategory_name_id_7f1df8f0_fk_category_ FOREIGN KEY (subcategory_name_id) REFERENCES public.category_sub_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_variationoffer offer_variationoffer_variation_name_id_0189e439_fk_store_var; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_variationoffer
    ADD CONSTRAINT offer_variationoffer_variation_name_id_0189e439_fk_store_var FOREIGN KEY (variation_name_id) REFERENCES public.store_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: offer_vendoroffer offer_vendoroffer_vendor_name_id_6f7cb1a7_fk_vendors_v; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.offer_vendoroffer
    ADD CONSTRAINT offer_vendoroffer_vendor_name_id_6f7cb1a7_fk_vendors_v FOREIGN KEY (vendor_name_id) REFERENCES public.vendors_vendors(vendor_id_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_order order_order_payment_id_d8fb3a38_fk_order_payment_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_order
    ADD CONSTRAINT order_order_payment_id_d8fb3a38_fk_order_payment_id FOREIGN KEY (payment_id) REFERENCES public.order_payment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_order order_order_user_id_7cf9bc2b_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_order
    ADD CONSTRAINT order_order_user_id_7cf9bc2b_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_order_id_18dae3b0_fk_order_order_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_order_id_18dae3b0_fk_order_order_id FOREIGN KEY (order_id) REFERENCES public.order_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_payment_id_13b3c50a_fk_order_payment_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_payment_id_13b3c50a_fk_order_payment_id FOREIGN KEY (payment_id) REFERENCES public.order_payment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_products_id_ee6c5f04_fk_store_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_products_id_ee6c5f04_fk_store_product_id FOREIGN KEY (products_id) REFERENCES public.store_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_user_id_d5f4875a_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_user_id_d5f4875a_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_variation_id_2e3db5f4_fk_store_variation_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_variation_id_2e3db5f4_fk_store_variation_id FOREIGN KEY (variation_id) REFERENCES public.store_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_orderproduct order_orderproduct_vendor_id_7c016ce6_fk_vendors_v; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_orderproduct
    ADD CONSTRAINT order_orderproduct_vendor_id_7c016ce6_fk_vendors_v FOREIGN KEY (vendor_id) REFERENCES public.vendors_vendors(vendor_id_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_payment order_payment_user_id_51d05b30_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.order_payment
    ADD CONSTRAINT order_payment_user_id_51d05b30_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_banners store_banners_vendor_id_6bbceeb2_fk_vendors_v; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_banners
    ADD CONSTRAINT store_banners_vendor_id_6bbceeb2_fk_vendors_v FOREIGN KEY (vendor_id) REFERENCES public.vendors_vendors(vendor_id_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_product store_product_category_id_574bae65_fk_category_category_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_product
    ADD CONSTRAINT store_product_category_id_574bae65_fk_category_category_id FOREIGN KEY (category_id) REFERENCES public.category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_product store_product_vendor_id_f9abf9af_fk_vendors_v; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_product
    ADD CONSTRAINT store_product_vendor_id_f9abf9af_fk_vendors_v FOREIGN KEY (vendor_id) REFERENCES public.vendors_vendors(vendor_id_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_reviewrating store_reviewrating_user_id_da0ed849_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_reviewrating
    ADD CONSTRAINT store_reviewrating_user_id_da0ed849_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_reviewrating store_reviewrating_varient_id_df5e34f2_fk_store_variation_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_reviewrating
    ADD CONSTRAINT store_reviewrating_varient_id_df5e34f2_fk_store_variation_id FOREIGN KEY (varient_id) REFERENCES public.store_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_variation store_variation_color_id_9a8c70b6_fk_store_varientcolor_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_variation
    ADD CONSTRAINT store_variation_color_id_9a8c70b6_fk_store_varientcolor_id FOREIGN KEY (color_id) REFERENCES public.store_varientcolor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_variation store_variation_product_id_e4f08cbc_fk_store_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.store_variation
    ADD CONSTRAINT store_variation_product_id_e4f08cbc_fk_store_product_id FOREIGN KEY (product_id) REFERENCES public.store_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_address user_address_user_id_64deb2c7_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_address
    ADD CONSTRAINT user_address_user_id_64deb2c7_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile user_profile_user_id_8fdce8e2_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile
    ADD CONSTRAINT user_profile_user_id_8fdce8e2_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vendors_vendors vendors_vendors_vendor_id_id_bba2a4b1_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.vendors_vendors
    ADD CONSTRAINT vendors_vendors_vendor_id_id_bba2a4b1_fk_account_account_id FOREIGN KEY (vendor_id_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

